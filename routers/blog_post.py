from fastapi import APIRouter

router = APIRouter(
    prefix="/bloag",
    tags=["blog"]
)

@router.post("/new")
def create_blog():
    pass