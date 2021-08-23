from fastapi import APIRouter, Request
from app.error.exceptions import FastException
from fastapi.responses import JSONResponse


router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/{username}", tags=["users"])
async def read_user(username: str):
    if username == 'error':
        raise FastException(name=username)
    return {"username": username}