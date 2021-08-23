import logging
import uvicorn

from app.internal import admin
from app.routers import items, users, redis, maria, sqlite
from app.server import app, responses

from app.logs.logging import FastLogger, config

logger = logging.getLogger('uvicorn.error')

app.include_router(users.router, responses={4042: {"description": "Not found"}},)
app.include_router(items.router)
app.include_router(redis.router)
app.include_router(maria.router)
app.include_router(sqlite.router)

app.include_router(admin.router)
app.logger = FastLogger()

@app.get("/")
async def start():
    logger.info('testsetse')
    return {"message": "Hello Bigger Applications!"}


# @app.on_event("startup")
# async def startup_event():
#     FastLogger()


if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, reload=True)
