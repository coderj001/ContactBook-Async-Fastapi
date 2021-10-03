from fastapi import APIRouter

from app.schema.contactbook import ContactBookSchema
from models.contactbook import ContactBook

router = APIRouter()


@router.get("/")
async def index():
    return {"message": "Hello"}


@router.post("/", response_model=ContactBookSchema)
async def create_contactbook(contactbook: ContactBookSchema):
    print(contactbook)
    return None
