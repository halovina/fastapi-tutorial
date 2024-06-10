from fastapi import APIRouter
from models.items import models
from .controllers import ItemException


router = APIRouter(
    prefix = '/items',
    tags = ['items'],
    responses = {
        404: {
            "message": "page not found"
        }
    }
)



@router.put("/{item_id}")
async def update_items(item_id: int, item: models.Item):
    results = {
        "item_id": item_id,
        "item": item
    }
    
    return results


items = {"foo": "The Foo Wrestlers"}


@router.get("/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise ItemException(item_id)
    return {"item": items[item_id]}
