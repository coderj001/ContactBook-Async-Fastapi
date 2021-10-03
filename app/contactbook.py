from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schema.contactbook import ContactBookResSchema, ContactBookSchema
from core.application import get_session
from models.contactbook import ContactBook


router = APIRouter()


@router.get("/")
async def index():
    return {"message": "Hello"}


@router.post("/", response_model=ContactBookResSchema)
async def create_contactbook(contactbook: ContactBookSchema, session: AsyncSession = Depends(get_session)):
    ct_book = await ContactBook.create(
        session,
        name=contactbook.name,
        email=contactbook.email
    )
    try:
        await session.commit()
        return ct_book
    except Exception as ex:
        await session.rollback()
        print(ex)
