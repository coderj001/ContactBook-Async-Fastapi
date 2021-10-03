from fastapi import APIRouter
from models.contactbook import Sample

router = APIRouter()


@router.get("/")
async def index():
    return {"message": "Hello"}
