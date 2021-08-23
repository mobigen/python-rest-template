import pytest

from fastapi import status
from fastapi.testclient import TestClient
from fastapi.responses import JSONResponse
from httpx import AsyncClient
from mock import patch


@patch('fastapi.testclient.TestClient.get',
       return_value={'row': [{'NAME': '123'}], 'status_code': 201})
def test_maria(maria_mock):
    from app.routers.maria import router
    real_data = TestClient(router).get(url="/maria")

    assert real_data.get('status_code') == 201
    assert real_data.get('row') == [{'NAME': '123'}]


@patch('fastapi.testclient.TestClient.get',
       return_value={"row": [{"NAME": "test12"}], 'status_code': 201})
def test_sqlite(sql_mock):
    from app.routers.sqlite import router
    real_data = TestClient(router).get(url="/sqlite")

    assert real_data.get('status_code') == 201
    assert real_data.get('row') == [{'NAME': 'test12'}]


@pytest.mark.asyncio
@patch('httpx.AsyncClient.get',
       return_value={"keys": ["a99ea9a3-7f92-470d-8c31-6bfca7aaef43_status",
                              "a99ea9a3-7f92-470d-8c31-6bfca7aaef43_result"]})
async def test_redis(redis_mock):
    from app.routers.redis import router

    async with AsyncClient(app=router, base_url="/redis") as ac:
        real_data = await ac.get("/keys")

    assert real_data.get('keys') == ["a99ea9a3-7f92-470d-8c31-6bfca7aaef43_status",
                                      "a99ea9a3-7f92-470d-8c31-6bfca7aaef43_result"]
