from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"intem_id": item_id, "q": q}

@app.get("/search_product_for_code/{product_code}")
def search_product_for_code(product_code: str):
    return {"product_code": product_code}
