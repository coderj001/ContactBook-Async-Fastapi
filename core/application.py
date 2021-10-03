from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import async_session


def create_api(*args, **kwargs) -> FastAPI:
    api = FastAPI(*args, **kwargs)
    return api


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
