from fastapi import APIRouter, Depends, HTTPException
from database.db_factory import get_db
from repository.token import TokenDAL
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from database.db import SessionLocal


router = APIRouter(
    prefix="/token",
    tags=["token"],
    responses={404: {"description": "Not found"}},
)

db = SessionLocal()


@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = TokenDAL(db).auth(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = TokenDAL(db).create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}