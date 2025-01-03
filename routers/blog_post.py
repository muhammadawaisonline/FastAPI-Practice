from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

router = APIRouter(
    prefix="/bloag",
    tags=["blog"]
)

class BlogModel(BaseModel):
    title:str
    content:str
    nb_comments:int
    published:Optional[bool]

@router.post("/new")
def create_blog(blog: BlogModel):
    blog.title
    return {"data":blog}