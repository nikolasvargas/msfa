from typing import Dict
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def index() -> Dict[str, str]:
    return {"Foo": "Bar"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None) -> Dict[int, str]:
    return {"item_id": item_id, "q": q}
