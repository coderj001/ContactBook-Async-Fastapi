from sqlalchemy import Column, String
from sqlalchemy.ext.asyncio import AsyncSession
from core.application import get_session

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
        pass
