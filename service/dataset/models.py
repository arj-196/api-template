from pydantic import BaseModel, Field


class Dataset(BaseModel):
    id: str
    name: str
    description: str | None = None
    meta: dict | None = None


class ReqCreateDataset(BaseModel):
    name: str
    description: str | None = None
    meta: dict | None = None
