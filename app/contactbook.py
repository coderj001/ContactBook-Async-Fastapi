from typing import List

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.schema.contactbook import ContactBookResSchema, ContactBookSchema, ContactBookUpdateSchema
from core.application import get_session
from models.contactbook import ContactBook

router = APIRouter()


@router.get("/", response_model=List[ContactBookResSchema])
async def index():
    return {"message": "Hello"}


@router.post("/", response_model=ContactBookResSchema)
async def create_contactbook(contactbook: ContactBookSchema, session: AsyncSession = Depends(get_session)):
    try:
        ct_book = await ContactBook.create(
            session,
            name=contactbook.name,
            email=contactbook.email
        )
        await session.commit()
        return ct_book
    except Exception as ex:
        await session.rollback()
        print(ex)


@router.delete("/")
async def delete_contactbook(id: int, session: AsyncSession = Depends(get_session)):
    try:
        await ContactBook.delete(session, id=id)
        await session.commit()
        return JSONResponse(
            status_code=202,
            content={
                'message': f'ContactBook Delete {id}'
            }
        )
    except Exception as ex:
        await session.rollback()
        print(ex)
        return JSONResponse(status_code=404, content={'message': 'Not Found!'})


@router.put("/", response_model=ContactBookResSchema)
async def update_contactbook(contactbook: ContactBookUpdateSchema, session: AsyncSession = Depends(get_session)):
    pass
