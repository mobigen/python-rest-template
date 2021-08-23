from fastapi import APIRouter, BackgroundTasks, Depends

from app.dependencies import get_token_header

router = APIRouter(
    prefix="/root",
    tags=["root"],
    # dependencies=[Depends(get_token_header)],
)


def write_notification(email: str, message=""):
    with open("/Users/jheok/Desktop/fast_template/log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)


@router.get("/")
async def root():
    BackgroundTasks.add_task(func=write_notification, email="test", message="some notification")
    return {"message": "Hello Bigger Applications!"}
