from pydantic import EmailStr
from typing import List, Optional
from .domain import  UserRecord

class UserRepository():
    def __init__(self):
        self._users: List[UserRecord] = []
        self._id_counter: int = 1


    def create(self, email: EmailStr, password: str):
        user: UserRecord = {
             "id": self._id_counter, 
             "email": email, 
             "password": password
             }
        
        self._users.append(user)
        self._id_counter += 1
        return user

    def get_by_email(self, email: str) -> Optional[UserRecord]:
        for user in self._users:
            if user["email"] == email:
                return user
        return None