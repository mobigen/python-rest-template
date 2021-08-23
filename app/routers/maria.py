from fastapi import APIRouter

from app.database.maria_conn import Maria

router = APIRouter(
    prefix="/maria",
    tags=["maria"],
    # dependencies=[Depends(get_token_header)],
)
router.database = Maria.get_instance()


@router.get("/", tags=["maria"])
async def select_table():
    row = router.database.execute(f"SELECT NAME FROM ANGORA_DATAMODELS where NAME = 'test_jjd'").fetchone()
    return {"row": [row], "status_code": 200}
