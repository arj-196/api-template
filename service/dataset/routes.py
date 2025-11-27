from logging import getLogger

from fastapi import APIRouter, Depends
from fastapi.params import Param, Path
from starlette.responses import JSONResponse

from api.auth import get_current_user

from .db import create_dataset, delete_dataset, get_dataset
from .models import Dataset, ReqCreateDataset

logger = getLogger()
router = APIRouter(prefix="/dataset", tags=["dataset"])


@router.get("", response_model=Dataset)
async def _get_dataset(
    name: str | None = None,
    id_: str | None = Param(alias="id", default=None),
    _=Depends(get_current_user),
):
    dataset = await get_dataset(name=name, id_=id_)
    if dataset is None:
        return JSONResponse(status_code=404, content={"message": "dataset not found"})
    return dataset


@router.post("", response_model=Dataset)
async def _create_dataset(item: ReqCreateDataset, _=Depends(get_current_user)):
    dataset = await get_dataset(name=item.name)
    if dataset is not None:
        return JSONResponse(
            status_code=409, content={"message": "dataset already exists"}
        )

    # create dataset
    dataset = await create_dataset(
        name=item.name, description=item.description, meta=item.meta
    )

    return dataset


@router.delete("")
async def _delete_dataset(
    name: str | None = None,
    id_: str | None = Param(alias="id", default=None),
    _=Depends(get_current_user),
):
    dataset = await get_dataset(name=name, id_=id_)
    if dataset is None:
        return JSONResponse(status_code=404, content={"message": "dataset not found"})

    # delete dataset
    await delete_dataset(dataset.name)
    return JSONResponse(status_code=200, content={"message": "dataset deleted"})
