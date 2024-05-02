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

def convert_to_product_type(tuple):
    produto_convertido = Produto(tuple)
    return produto_convertido

tupla = (2, '7896741313348', None, 'TUBO EXT.P/CORTINA 1,20A1,33 MT', None, 'MAXEB', None, Decimal('10.7500'), Decimal('10.7500'), Decimal('21.9900'), -3.0, 1.0, 'UN', 104.56, 0.0, None, '2018-08-15', None, None, False, False, '83024900', 0.0, '102', 18.0, 100.0, 0.38, 0.38, None, None, None, None, None, None, datetime(2017, 1, 13, 17, 20, 30), 1, None, 0.0, None, None, 0.0, '7896741313348', '7896741313348', None, None, 0, None, None)

retorno = convert_to_product_type(tupla)
print(retorno)