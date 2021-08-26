from app.init.config import *
from app.init.log import *
from app.server import *
from app.routers import *


def start():
    import uvicorn
    from app.config.base_config import Config

    uvicorn.run(
        "main:app",
        port=Config.server.port,
        workers=Config.server.workers,
        log_config=log_config
    )


if __name__ == "__main__":
    # print(dir(logging.Logger.manager.loggerDict))
    # print(logging.Logger.manager.loggerDict)
    start()
