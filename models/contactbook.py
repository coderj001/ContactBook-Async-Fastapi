from sqlalchemy import Column, String, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from models.base import AuditMixin


class ContactBook(AuditMixin):
    __tablename__ = "contactbook"

    name = Column(String(), server_default='', nullable=False)
    email = Column(String(), unique=True, nullable=False)

    @classmethod
    async def create(cls, session: AsyncSession, **kwargs):
        ct_book = cls(**kwargs)
        session.add(ct_book)
        return ct_book

    @classmethod
    async def get(cls, session: AsyncSession, **kwargs):
        if kwargs.get('id'):
            ct_book = await session.execute(
                select(cls).where(cls.id == kwargs.get('id')))
            return ct_book.fetchone()[0]

    @classmethod
    async def update(cls, session: AsyncSession, **kwargs):
        if kwargs.get('id'):
            id = kwargs.pop('id')
            ct_book = await session.execute(
                update(cls).where(cls.id == id)
                .values(**kwargs).returning(cls)
            )
            return ct_book.fetchone()[0]

    @classmethod
    async def find(cls, session: AsyncSession, **kwargs):
        pagination = 10
        if kwargs.get('page'):
            page = int(kwargs.pop('page')) - 1
        else:
            page = 0
        if (
            kwargs.get('name') and kwargs.get('email')
        ) or (
            kwargs.get('name') or kwargs.get('email')
        ):
            if kwargs.get('name') and kwargs.get('email') is None:
                ct_book = await session.execute(
                    select(cls.id,
                           cls.name,
                           cls.email
                           )
                    .where(cls.name.like(f"{kwargs.get('name')}%"))
                    .offset(page*pagination)
                    .limit(10)
                )
            if kwargs.get('name') is None and kwargs.get('email'):
                ct_book = await session.execute(
                    select(cls.id,
                           cls.name,
                           cls.email
                           )
                    .where(cls.email.like(f"{kwargs.get('email')}%"))
                    .offset(page*pagination)
                    .limit(10)
                )
            else:
                ct_book = await session.execute(
                    select(cls.id,
                           cls.name,
                           cls.email
                           ).where(
                        cls.email.like(f"{kwargs.get('email')}%"),
                        cls.name.like(f"{kwargs.get('name')}%")
                    )
                    .offset(page*pagination).limit(10)
                )
        else:
            ct_book = await session.execute(
                select(
                    cls.id,
                    cls.name,
                    cls.email
                )
                .offset(int(page)*pagination)
                .limit(10)
            )
        return ct_book.fetchmany()
