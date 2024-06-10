from fastapi import APIRouter
from models.items import models


router = APIRouter(
    prefix = '/items',
    tags = ['items'],
    responses = {
        404: {
            "message": "page not found"
        }
    }
)

@router.put("/item_id")
async def update_items(item_id: int, item: models.Item):
    results = {
        "item_id": item_id,
        "item": item
    }
    
    return results