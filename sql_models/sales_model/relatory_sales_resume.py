from pydantic import BaseModel
from datetime import date, datetime

class RelatorySalesResume(BaseModel):
    data : date
    valor_venda : float | None
    troco : float | None
    valor_liquido : float | None

class MethodRelatoryResume():
    def __init__(self) -> None:
        pass

    def convert_to_relatory(tuple):
        sales_convert = RelatorySalesResume(**{key: tuple[i] for i, key in enumerate(RelatorySalesResume.model_fields.keys())})
        return sales_convert