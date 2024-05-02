from typing import Union
from fastapi import FastAPI
from sql_server_connection import ConnectionDatabase

app = FastAPI()
connection_db = ConnectionDatabase()

@app.get("/")
def read_root():
    return {"API_status": "active"}

@app.get("/search_product_for_code/{product_code}")
def search_product_for_code(product_code: str):
    return_product_data = connection_db.get_product_by_code(product_code)
    return return_product_data

@app.get("/search_product_for_description/{product_description}")
def search_product_for_code(product_description: str):
    return_products_data = connection_db.get_product_by_description(product_description)
    return return_products_data
