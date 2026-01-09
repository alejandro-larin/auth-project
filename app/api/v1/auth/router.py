from fastapi  import APIRouter
from .schemas import UserCreateRequest, UserResponse
from .service import auth_service
router: APIRouter = APIRouter()

@router.post("/register", response_model=UserResponse)
async def register_user(payload: UserCreateRequest) -> UserResponse:
    return auth_service.register_user(payload)