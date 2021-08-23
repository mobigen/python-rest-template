from fastapi.testclient import TestClient

from app.routers.items import router


client = TestClient(router)


def test_read_item():
    response = client.get(url="/items/foo", headers={"X-Token": "header_token"})
    print(response)
    assert response.status_code == 200
    assert response.json() == {
        "id": "foo",
        "title": "foo",
        "description": "foofoofoofoo",
    }


# def test_read_item_bad_token():
#     response = client.get(url="/items/foo", headers={"X-Token": "nononono"})
#     print(response.status_code)
#     print(response.json())
#     assert response.status_code == 400
#     assert response == {"detail": "X-Token header invalid"}


