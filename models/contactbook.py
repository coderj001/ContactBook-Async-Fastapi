from sqlalchemy import Column, String, delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from models.base import AuditMixin


class ContactBook(AuditMixin):
    __tablename__ = "contactbook"

    name = Column(String(), server_default='', nullable=False)
    email = Column(String(), unique=True, nullable=False)

    @classmethod
    async def create(cls, session: AsyncSession, **kwargs):
        ct_book = ContactBook(**kwargs)
        session.add(ct_book)
        return ct_book

    @classmethod
    async def get(cls, session: AsyncSession, **kwargs):
        if kwargs.get('id'):
            ct_book = await session.execute(
                select(ContactBook).where(ContactBook.id == kwargs.get('id')).limit(1))
        return ct_book

    @classmethod
    async def delete(cls, session: AsyncSession, **kwargs):
        if kwargs.get('id'):
            await session.execute(
                delete(ContactBook).where(ContactBook.id == kwargs.get('id')))
