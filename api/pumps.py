from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.db_factory import get_db
from repository.pumps import PumpsDAL
from dto.pumps import pumps

router = APIRouter(
    prefix="/pumps",
    tags=["pumps"],
    responses={404: {"description": "Not found"}},
)


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
