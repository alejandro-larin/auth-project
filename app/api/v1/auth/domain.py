from typing import TypedDict
from pydantic import EmailStr

class UserRecord(TypedDict):
    id: int
    email: EmailStr
    password: str
