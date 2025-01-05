from fastapi import APIRouter, Query, Body
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

@router.post("/new/{id}")
def create_blog(blog: BlogModel, id:int, version:int = 1):
    blog.title
    return {
        "id":id,
        "version":version,
        "data":blog}

@router.post("/new/{id}/comment")
def create_comment(blog: BlogModel, id:int, comment_id=Query(

    title = "Id of the comment",
    description= "Some description of the comment_id",
    alias= "commentId"
), 
    content:str = Body(...,
                       min_length=10,
                       max_length=50) ):
    return {
        "blog": blog,
        "id": id,
        "comment_id": comment_id,
        "content": content
    }