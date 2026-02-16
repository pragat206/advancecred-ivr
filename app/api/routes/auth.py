from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.auth.security import create_access_token, verify_password
from app.db.models import User
from app.db.session import get_db
from app.models.schemas import LoginRequest, LoginResponse, RoleType

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=LoginResponse)
def login(payload: LoginRequest, db: Session = Depends(get_db)) -> LoginResponse:
    user = db.query(User).filter(User.email == payload.email).first()
    if not user or not verify_password(payload.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token = create_access_token(subject=user.email, tenant_id=user.tenant_id, role=user.role.value)
    return LoginResponse(access_token=token, role=RoleType(user.role.value), tenant_id=user.tenant_id)
