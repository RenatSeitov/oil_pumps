from models.users import Users
from sqlalchemy.orm import Session
from dto.users.users import UserCreate
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserDAL:
    def __init__(self, db: Session):
        self.db_session = db

    def add_user(self, data: UserCreate):
        hashed_password = pwd_context.hash(data.password)
        user = Users(username=data.username, fast_name=data.fast_name,
                     last_name=data.last_name, password=hashed_password)
        self.db_session.add(user)
        self.db_session.commit()
        self.db_session.refresh(user)
        response = {'username': data.username, 'fast_name': data.fast_name, 'last_name': data.last_name}
        return response

    def get_user_by_username(self, username: str):
        user = self.db_session.query(Users).filter_by(username=username).first()
        if user:
            return {'username': user.username, 'fast_name': user.fast_name, 'last_name': user.last_name}
