from pydantic import BaseModel
from datetime import date, datetime

class RelatorySalesDetailed(BaseModel):
    data : date
    pedido : int
    recebimento : str
    valor_venda : float | None
    troco : float | None
    valor_liquido : float | None

class MethodRelatoryDetailed():
    def __init__(self) -> None:
        pass

    def convert_to_relatory(tuple):
        sales_convert = RelatorySalesDetailed(**{key: tuple[i] for i, key in enumerate(RelatorySalesDetailed.model_fields.keys())})
        return sales_convert