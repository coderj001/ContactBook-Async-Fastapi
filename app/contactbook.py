from typing import List, Optional

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.schema.contactbook import ContactBookResSchema, ContactBookSchema, ContactBookUpdateSchema
from core.application import get_session
from models.contactbook import ContactBook

router = APIRouter()


@router.get("/", response_model=List[ContactBookResSchema])
async def find_contactbook(page: int = 1, name: str = None, email: str = None, session: AsyncSession = Depends(get_session)):
    return await ContactBook.find(
        session,
        page=page,
        name=name,
        email=email
    )


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


@router.delete("/{id}", response_model=ContactBookResSchema)
async def delete_contactbook(id: int, session: AsyncSession = Depends(get_session)):
    try:
        ct_book = await ContactBook.get(session, id=id)
        await session.delete(ct_book)
        await session.commit()
        return ct_book
    except Exception as ex:
        await session.rollback()
        print(ex)
        return JSONResponse(status_code=404, content={'message': 'Not Found!'})


@router.put("/{id}", response_model=ContactBookResSchema)
async def update_contactbook(id: int, contactbook: ContactBookUpdateSchema, session: AsyncSession = Depends(get_session)):
    try:
        ct_book = await ContactBook.update(
            session,
            id=id,
            name=contactbook.name,
            email=contactbook.email
        )
        await session.commit()
        return await ContactBook.get(session, id=ct_book)
    except Exception as ex:
        await session.rollback()
        print(ex)
        return JSONResponse(status_code=404, content={'message': 'Not Found!'})
