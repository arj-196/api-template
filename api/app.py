from logging import getLogger

from fastapi import FastAPI

import service.dataset.routes

from .utils import get_version

app = FastAPI(
    title="Api Template",
    version=get_version(),
)

logger = getLogger()


@app.get("/")
async def read_root():
    return {"status": "ok", "body": "Api Template", "version": get_version()}


app.include_router(service.dataset.routes.router)
