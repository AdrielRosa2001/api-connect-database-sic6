from typing import Union
from fastapi import FastAPI
from sql_server_connection import ConnectionDatabase
from sql_models.sales_model.sales_search import SalesSearch
from sql_models.sales_model.relatory_sales_resume import RelatorySalesResume

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

@app.get("/search_type_sales")
def search_sales_for_dates():
    return_types_sales = connection_db.get_type_sales()
    return return_types_sales

@app.post("/search_sales_for_dates/")
def search_sales_for_dates(sales_search: SalesSearch):
    return_sales = connection_db.get_sales_not_note(sales_search)
    return return_sales

@app.get("/search_relatory_resume/{date_search}")
def search_relatory_sales_resume(date_search: str):
    return_relatory = connection_db.get_relatory_sales_resume(date_search)
    return return_relatory

@app.get("/search_relatory_types/{date_search}")
def search_relatory_sales_types(date_search: str):
    return_relatory = connection_db.get_relatory_sales_types_received(date_search)
    return return_relatory

@app.get("/search_relatory_detailed/{date_search}")
def search_relatory_sales_detailed(date_search: str):
    return_relatory = connection_db.get_relatory_sales_detailed(date_search)
    return return_relatory