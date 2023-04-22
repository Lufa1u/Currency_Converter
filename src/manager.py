import requests
from sqlalchemy.orm import Session
from sqlalchemy import or_
import config
from src.models import CurrencyConverter
import json
from src.schemas import CurrencySchema, CurrencyConvertSchema


async def convert_currency(convert: CurrencyConvertSchema, db: Session):
    # что бы сразу работало
    if not db.query(CurrencyConverter).all():
        await load_all_currencies(db=db)

    rates = dict([item for item in db.query(CurrencyConverter.rate, CurrencyConverter.code).filter(
        or_(CurrencyConverter.code == convert.source, CurrencyConverter.code == convert.target)).all()])
    rates = dict(zip(rates.values(), rates.keys()))
    return convert.amount * ((convert.amount * rates[convert.target]) / (convert.amount * rates[convert.source]))


async def get_all_currency_rates(db: Session):
    # что бы сразу работало
    if not db.query(CurrencyConverter).all():
        await load_all_currencies(db=db)

    result = []
    all_currency_rates = db.query(CurrencyConverter).all()
    for currency_rate in all_currency_rates:
        result.append(CurrencySchema(**currency_rate.__dict__))
    return result


async def load_all_currencies(db: Session):
    db.query(CurrencyConverter).delete()
    db.commit()
    url = "https://api.apilayer.com/exchangerates_data/latest?&base=USD"
    headers = {"apikey": config.API_KEY}
    names = await get_names()
    rates = (json.loads((requests.get(url=url, headers=headers)).text))["rates"]
    for code, rate in rates.items():
        model = CurrencyConverter(name=names[code], code=code, rate=rate)
        db.add(model)
    db.commit()


async def get_names():
    url = "https://api.apilayer.com/exchangerates_data/symbols"
    headers = {"apikey": config.API_KEY}
    return (json.loads((requests.get(url=url, headers=headers)).text))["symbols"]

