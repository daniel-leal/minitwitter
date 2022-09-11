import bcrypt
from fastapi import APIRouter
from fastapi_sqlalchemy import db

from model import User as ModelUser
from schema import User as Users
from schema import UserCreate as SchemaUser

router = APIRouter()


@router.post("/register", response_model=Users)
async def create_user(user: SchemaUser):
    hashed_password = bcrypt.hashpw(
        user.password.encode("utf-8"), bcrypt.gensalt()
    )
    User = ModelUser(
        first_name=user.first_name,
        last_name=user.last_name,
        username=user.username,
        email=user.email,
        password=hashed_password,
    )
    db.session.add(User)
    db.session.commit()
    db.session.refresh(User)
    return User
