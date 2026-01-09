from fastapi import APIRouter
from .v1.auth.router import router as auth_router

api_router: APIRouter = APIRouter(prefix="/api/v1")

api_router.include_router(auth_router , prefix="/auth", tags=["Authentication"])
# api_router.include_router(auth_router ,prefix="/users", tags=["Users"])