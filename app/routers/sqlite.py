from fastapi import APIRouter

from app.database.sqlite_conn import Sqlite

router = APIRouter(
    prefix="/sqlite",
    tags=["sqlite"],
    # dependencies=[Depends(get_token_header)],
)
router.database = Sqlite.get_instance()


@router.get("/", tags=["sqlite"])
async def schema():
    row = router.database.execute(f"SELECT NAME FROM ANGORA_DATAMODELS LIMIT 1").fetchone()
    return {"row": [row]}
