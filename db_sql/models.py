from datetime import datetime

from sqlalchemy import JSON, DateTime, MetaData, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from service.dataset.models import Dataset

meta = MetaData()


class Base(DeclarativeBase):
    metadata = meta


class DatasetTable(Base):
    __tablename__ = "datasets"
    created_at: Mapped[datetime] = mapped_column(DateTime())
    id: Mapped[str] = mapped_column(String(100), primary_key=True, unique=True)

    name: Mapped[str] = mapped_column(String(100), unique=True)
    description: Mapped[str] = mapped_column(Text(), nullable=True)
    meta: Mapped[dict] = mapped_column(JSON(), nullable=True)

    def to_model(self) -> Dataset:
        return Dataset(
            id=self.id,
            name=self.name,
            description=self.description,
            meta=self.meta,
        )
