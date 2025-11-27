from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from common.settings import get_settings

http_bearer = HTTPBearer()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(http_bearer),
):
    token = credentials.credentials
    if not token or token != get_settings().api_key.get_secret_value():
        raise HTTPException(status_code=401, detail="Not authenticated")
    return {"email": "internal"}
