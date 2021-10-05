from fastapi import APIRouter
from app.error.exceptions import FastException
from app.server import app
from app.config.base_config import Config
import logging

logger = logging.getLogger()

logger.info(Config.server.port)
logger.info('init user')

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@app.get("/")
def test():
    return [{"username": "Rickaa"}, {"username": "Morty"}]


@router.get("/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/{username}", tags=["users"])
async def read_user(username: str):
    if username == 'error':
        raise FastException(name=username)
    return {"username": username}