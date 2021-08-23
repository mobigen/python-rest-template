from fastapi import APIRouter, Depends, HTTPException

from app.dependencies import get_token_header
from app.database.redis_conn import rcline


router = APIRouter(
    prefix="/redis",
    tags=["redis"],
    # dependencies=[Depends(get_token_header)],
)


@router.get("/")
async def read_item():
    redis_keys = []
    for key in rcline.scan_iter(match='*', count=100):
        redis_keys.append(key)

    return {"keys": redis_keys}
