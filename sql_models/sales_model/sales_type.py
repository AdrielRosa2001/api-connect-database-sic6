from pydantic import BaseModel

class SalesType(BaseModel):
    controle : int
    recebimento : str
    fixo : bool | None

class MethodsTypesSales():
    def __init__(self) -> None:
        pass

    def convert_to_sales_types(tuple):
        types_convert = SalesType(**{key: tuple[i] for i, key in enumerate(SalesType.model_fields.keys())})
        return types_convert