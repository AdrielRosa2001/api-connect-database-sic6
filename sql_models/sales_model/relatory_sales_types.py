from pydantic import BaseModel
from datetime import date, datetime

class RelatorySalesTypes(BaseModel):
    data : date
    recebimento : str
    valor_venda : float | None
    troco : float | None
    valor_liquido : float | None

class MethodRelatoryTypes():
    def __init__(self) -> None:
        pass

    def convert_to_relatory(tuple):
        sales_convert = RelatorySalesTypes(**{key: tuple[i] for i, key in enumerate(RelatorySalesTypes.model_fields.keys())})
        return sales_convert