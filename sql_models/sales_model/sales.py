from pydantic import BaseModel
from datetime import date, datetime

class Sales(BaseModel):
    data : date
    nota : int | None
    pedido : int
    lkreceb : int

class MethodsSales():
    def __init__(self) -> None:
        pass

    def convert_to_sales(tuple):
        sales_convert = Sales(**{key: tuple[i] for i, key in enumerate(Sales.model_fields.keys())})
        return sales_convert