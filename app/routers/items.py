from fastapi import APIRouter, Depends, HTTPException

from app.dependencies import get_token_header

router = APIRouter(
    prefix="/items",
    tags=["items"],
    # dependencies=[Depends(get_token_header)],
)


@router.get("/{item_id}")
async def read_item(item_id: str):
    if item_id != 'foo':
        return HTTPException(status_code=404, detail="Item not found")
    return {"id": item_id, "title": item_id, "description": item_id * 4}


@router.put(
    "/{item_id}",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
)
async def update_item(item_id: str):
    if item_id != "plumbus":
        raise HTTPException(
            status_code=403, detail="You can only update the item: plumbus"
        )
    return {"item_id": item_id, "name": "The great Plumbus"}