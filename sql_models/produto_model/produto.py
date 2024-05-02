from datetime import date, datetime
from pydantic import BaseModel
from decimal import Decimal

class Produto(BaseModel):
    id: int
    codigo: str | None
    codinterno: str | None
    produto: str | None
    Iksetor: int | None
    fabricante: str | None
    Ikfornec: int | None
    precocusto: float | None #money
    customedio: float | None #money
    precovenda: float | None #money
    quantidade: float | None
    estminimo: float | None
    unidade: str | None
    lucro: float | None
    comissao: float | None
    moeda: str | None
    ultreaj: date | None
    foto:  str | None
    obs: str | None
    naosaitabela: int | None
    inativo: int | None
    codipi: str | None
    ipi: float | None
    cst: str | None
    icms: float | None
    basecalculo: float | None
    pesobruto: float | None
    pesoliq: float | None
    Ikmodulo: int | None
    armazenamento: str | None
    qntembalagem: int | None
    elv: int | None
    previsao: date | None
    datafoto: datetime | None
    datainc: datetime | None
    Ikuserinc: int | None
    codex: str | None
    iva_st: float | None
    pfc: float | None
    ipi_cst: str | None
    ipi_basecalc: float | None
    cean: str | None
    ceantrib: str | None
    cprodanp: int | None
    cest: str | None
    origem: int | None
    CST_PIS: str | None
    CST_COFINS: str | None

class MetodosProduto():
    def __init__(self) -> None:
        pass
    
    def convert_to_product_type(tuple):
        produto_convertido = Produto(**{key: tuple[i] for i, key in enumerate(Produto.model_fields.keys())})
        return produto_convertido
    
#7896741313348