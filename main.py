from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Simple FastAPI Demo")


class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None


@app.get("/", tags=["root"])
async def read_root() -> dict:
    """Health-check / root endpoint"""
    return {"message": "FastAPI is running"}


@app.get("/items/{item_id}", response_model=Item, tags=["items"])
async def read_item(item_id: int) -> Item:
    """Return a dummy item for the given id"""
    # In a real app you'd fetch from a DB. Here we return a stub.
    if item_id <= 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return Item(id=item_id, name=f"Item {item_id}", description="A demo item")


@app.post("/items", response_model=Item, status_code=201, tags=["items"])
async def create_item(item: Item) -> Item:
    """Create an item and return it with a generated id"""
    # Normally you'd persist the item; we'll fake an id.
    item.id = 1
    return item
