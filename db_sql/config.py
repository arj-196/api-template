from typing import AsyncIterator

from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from common.settings import get_settings

engine = create_async_engine(
    get_settings().db_url_async,
    future=True,
    poolclass=NullPool,
)

async_session = async_sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
    future=True,
)


async def get_session() -> AsyncIterator[AsyncSession]:
    async with async_session() as session:
        yield session


async def close() -> None:
    await engine.dispose()
