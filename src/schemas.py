from pydantic import BaseModel


class CurrencySchema(BaseModel):
    name: str
    code: str
    rate: float


class CurrencyConvertSchema(BaseModel):
    source: str
    target: str
    amount: float
