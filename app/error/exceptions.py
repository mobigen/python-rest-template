from app.server import app
from fastapi import Request
from fastapi.responses import JSONResponse


class ConfigException(Exception):
    def __init__(self, key, value, msg):
        self.key = key
        self.value = value
        self.msg = msg


class FastException(Exception):
    def __init__(self, name: str):
        self.name = name


@app.exception_handler(FastException)
async def fast_exception_handler(request: Request, exc: FastException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )
