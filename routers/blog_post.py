from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/bloag",
    tags=["blog"]
)

class BlogModel(BaseModel):
    pass

@router.post("/new")
def create_blog():
    pass