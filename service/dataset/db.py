import uuid
from datetime import datetime
from logging import getLogger

from sqlalchemy import delete, select

from db_sql.config import async_session
from db_sql.models import DatasetTable

from .models import Dataset

logger = getLogger()


async def get_dataset(
    name: str | None = None, id_: str | None = None
) -> Dataset | None:
    if not name and not id_:
        return None

    async with async_session() as session:
        if name:
            condition = DatasetTable.name == name
        elif id_:
            condition = DatasetTable.id == id_

        dataset = (
            (await session.execute(select(DatasetTable).filter(condition)))
            .scalars()
            .one_or_none()
        )
        return dataset.to_model() if dataset else None


async def create_dataset(
    name: str, description: str | None = None, meta: dict | None = None
) -> Dataset:
    async with async_session() as session:
        dataset = DatasetTable(
            created_at=datetime.now(),
            id=str(uuid.uuid4()),
            name=name,
            description=description,
            meta=meta,
        )
        session.add(dataset)
        await session.commit()
        return dataset.to_model()


async def delete_dataset(name: str):
    async with async_session() as session:
        await session.execute(delete(DatasetTable).where(DatasetTable.name == name))
        await session.commit()
    return
