from fastapi import APIRouter, Query, Body
from pydantic import BaseModel
from typing import Optional, List

router = APIRouter(
    prefix="/blog",
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
def create_comment(blog: BlogModel, id:int, comment_id: int =Query(

    title = "Id of the comment",
    description= "Some description of the comment_id",
    alias= "commentId"
), 
    content:str = Body(...,
                       regex= "^[a-z\s]*$") ,
                       v: Optional[List[str]] = Query(["1.0", "1.1", "1.2 "])):
    return {
        "blog": blog,
        "id": id,
        "comment_id": comment_id,
        "content": content,
        "version": v
    }