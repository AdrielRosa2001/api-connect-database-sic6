from pydantic import BaseModel
from datetime import date, datetime

class SalesSearch(BaseModel):
    start_date : date
    end_date : date
    type_sale : int