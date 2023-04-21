from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dto.users import users
from database.db_factory import get_db
from repository.users import UserDAL


router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.post("/add_user")
def add_user(data: users.UserCreate, db: Session = Depends(get_db)):
    user = UserDAL(db).get_user_by_username(username=data.username)
    if not user:
        response = UserDAL(db).add_user(data)
        return response
