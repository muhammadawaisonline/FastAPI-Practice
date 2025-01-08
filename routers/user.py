from schemas import UserBase, UserDisplay
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_user

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

# @router.get("/", response_class= UserDisplay)
# def get_user(id:int, db:Session = Depends(get_db)):
#     return db_user.get_user(db, id)


# @router.post("/", response_class= UserDisplay)
# def create_user(request:UserBase, db:Session = Depends(get_db)):
#     return db_user.create_user(db, request)

@router.post("/", response_model=UserDisplay)
def create_user(request:UserBase, db:Session = Depends(get_db)):
    return db_user.create_user(db, request)