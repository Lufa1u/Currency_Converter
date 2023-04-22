import decimal

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.schemas import CurrencySchema, CurrencyConvertSchema
from db import get_db
from src import manager

router = APIRouter()


@router.get(path="/upload_to_database", status_code=200)
async def load_all_currency(db: Session = Depends(get_db)):
    await manager.load_all_currencies(db=db)


@router.get(path="/get_all_currency_rates", response_model=list[CurrencySchema])
async def get_all_currency_rates(db: Session = Depends(get_db)):
    return await manager.get_all_currency_rates(db=db)


@router.post(path="/convert_currency", response_model=float)
async def convert_currency(convert: CurrencyConvertSchema, db: Session = Depends(get_db)):
    return await manager.convert_currency(convert=convert, db=db)
