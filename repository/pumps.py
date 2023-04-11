from models.pimps import Pumps
from sqlalchemy.orm import Session


class PumpsDAL:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_data(self, idx: int):
        return self.db_session.query(Pumps).filter(Pumps.id == idx).first()

    def insert_data(self, data: Pumps):
        self.db_pump = Pumps(id=data.id, pressure=data.pressure,
                             temperature=data.temperature, speed=data.temperature)
        self.db_session.add(self.db_pump)
        self.db_session.commit()
        self.db_session.refresh(self.db_pump)
        return self.db_pump
