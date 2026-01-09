from .schemas import UserCreateRequest, UserResponse
from .repository import UserRepository
from .domain import UserRecord
from typing import Optional
from .security import hash_password

class AuthService:
    def __init__(self):
        self._user_repo: UserRepository = UserRepository()

    def register_user(self, payload: UserCreateRequest) -> UserResponse:

        existing_user: Optional[UserRecord] = (
            self._user_repo.get_by_email(payload.email)
        )


        if existing_user:
            raise ValueError("This user already exists")
        
        hashed: str = hash_password(payload.password)
        user_record: UserRecord = self._user_repo.create(email=payload.email, password=hashed)

        return UserResponse(
            id=user_record["id"],
            email=user_record["email"],
        )

auth_service = AuthService()