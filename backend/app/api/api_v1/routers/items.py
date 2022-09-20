from fastapi import APIRouter, Request, Depends, Response
import typing as t

from app.data.session import get_db
from app.data.repositories.item_repository import (
    get_items,
    get_item,
    create_item,
    edit_item,
    delete_item,
    get_items_summary,
)
from app.data.models import Item, ItemSummary

items_router = r = APIRouter()


@r.get(
    "/items/summary",
    response_model=ItemSummary,
    response_model_exclude_none=True,
)
async def item_summary(response: Response, db=Depends(get_db)):
    return get_items_summary(db)


@r.get(
    "/items",
    response_model=list[Item],
    response_model_exclude_none=True,
)
async def items_list(response: Response, db=Depends(get_db)):
    """
    Get all items
    """
    items = get_items(db)
    if len(items) == 4:
        print(items)
    # This is necessary for react-admin to work
    response.headers["Content-Range"] = f"0-9/{len(items)}"
    return items


@r.get(
    "/items/{item_id}", response_model=Item, response_model_exclude_none=True
)
async def item_get(
    request: Request,
    item_id: int,
    db=Depends(get_db),
):
    """
    Get any Item
    """
    return get_item(db, id=item_id)


@r.post("/items", response_model=Item, response_model_exclude_none=True)
async def item_create(request: Request, item: Item, db=Depends(get_db)):
    """
    Create a new item
    """
    return create_item(db, item)


@r.put(
    "/items/{item_id}", response_model=Item, response_model_exclude_none=True
)
async def item_edit(
    request: Request, item_id: int, item: Item, db=Depends(get_db)
):
    """
    Update existing item
    """
    return edit_item(db, item_id, item)


@r.delete(
    "/items/{item_id}", response_model=Item, response_model_exclude_none=True
)
async def item_delete(request: Request, item_id: int, db=Depends(get_db)):
    """
    Delete existing item
    """
    item = get_item(db, item_id)
    delete_item(db, item_id)
    return item
