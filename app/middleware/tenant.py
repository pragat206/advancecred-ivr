from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse


class TenantHeaderMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        public_paths = {"/health", "/", "/ui"}
        if request.url.path.startswith("/api/v1") and request.url.path not in {"/api/v1/auth/login"}:
            if request.headers.get("X-Tenant-ID") is None:
                return JSONResponse({"detail": "X-Tenant-ID header is required"}, status_code=400)
        if request.url.path in public_paths or request.url.path.startswith("/static"):
            return await call_next(request)
        return await call_next(request)
