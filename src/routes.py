from fastapi import APIRouter, Depends
from src.schemas import CurrencySchema
from src.manager import GetAllCurrency, ConvertCurrency
from dependency_injector.wiring import Provide, inject
from src.containers import CurrencyContainer
from src.schemas import CurrencyConvertSchema

router = APIRouter()


@router.get(path="/get_all_currency_rates", response_model=list[CurrencySchema])
@inject
async def get_all_currency_rates(
        get_all_currency: GetAllCurrency = Depends(Provide[CurrencyContainer.get_all_currency])
):
    return await get_all_currency.get_all_currency_rates()


@router.post(path="/convert_currency", response_model=float)
@inject
async def convert_currency(
        currency_convert_schema: CurrencyConvertSchema = Depends(CurrencyContainer.currency_convert_schema),
        convert_currency: ConvertCurrency = Depends(Provide[CurrencyContainer.convert_currency])
):
    return await convert_currency.convert_currency(currency_convert_schema)
