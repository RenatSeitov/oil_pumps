from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    fast_name: str | None = None
    last_name: str | None = None
    password: str


class Users(UserCreate):
    user_id: int
