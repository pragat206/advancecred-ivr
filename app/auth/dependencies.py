from dataclasses import dataclass

from fastapi import Depends, Header, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.models import User
from app.db.session import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


@dataclass
class CurrentUser:
    id: int
    email: str
    role: str
    tenant_id: int


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> CurrentUser:
    credentials_error = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid authentication credentials",
    )
    try:
        payload = jwt.decode(token, settings.jwt_secret, algorithms=[settings.jwt_algo])
        email = payload.get("sub")
        tenant_id = payload.get("tenant_id")
        role = payload.get("role")
    except JWTError as exc:
        raise credentials_error from exc

    user = db.query(User).filter(User.email == email, User.tenant_id == tenant_id).first()
    if not user or not user.is_active:
        raise credentials_error

    return CurrentUser(id=user.id, email=user.email, role=role, tenant_id=user.tenant_id)


def require_role(*allowed_roles: str):
    def checker(current: CurrentUser = Depends(get_current_user)) -> CurrentUser:
        if current.role not in allowed_roles:
            raise HTTPException(status_code=403, detail="Insufficient permissions")
        return current

    return checker


def enforce_tenant_header(current: CurrentUser = Depends(get_current_user), x_tenant_id: str | None = Header(default=None)) -> None:
    if x_tenant_id is None:
        raise HTTPException(status_code=400, detail="X-Tenant-ID header is required")
    if str(current.tenant_id) != x_tenant_id:
        raise HTTPException(status_code=403, detail="Tenant mismatch")
