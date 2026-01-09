from .schemas import UserCreateRequest, UserResponse

class AuthService:
    def register_user(self, payload: UserCreateRequest) -> UserResponse:

        return UserResponse(
                id=1,                
                email=payload.email
            )

auth_service = AuthService()