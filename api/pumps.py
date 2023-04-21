from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from database.db_factory import get_db
from repository.pumps import PumpsDAL
from repository.users import UserDAL
from dto.pumps import pumps


router = APIRouter(
    prefix="/pumps",
    tags=["pumps"],
    responses={404: {"description": "Not found"}},
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token/create")
# Настройка JWT
SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


@router.get("/pumps")
async def get_pumps_data(idx: int, db: Session = Depends(get_db)):
    data = PumpsDAL(db).get_data(idx=idx)
    return data


@router.post("/insert_pumps")
async def insert_pumps_data(data: pumps.Pumps, db: Session = Depends(get_db)):
    pumps = PumpsDAL(db).get_data(idx=data.id)
    if pumps:
        raise HTTPException(status_code=400, detail="Pumps already registered")
    return PumpsDAL(db).insert_data(data=data)


@router.get("/all_pumps")
async def get_pumps_all(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    user = UserDAL(db).get_user_by_username(username)
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    pumps = PumpsDAL(db).get_all()
    return {"user": pumps}
