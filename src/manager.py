import requests
from sqlalchemy import or_
import json
from fastapi import HTTPException
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


class Database:
    def __init__(self, url):
        self.url = url

    def get_db(self):
        engine = create_engine(self.url)
        SessionClass = sessionmaker(bind=engine)
        return SessionClass()


class LoadCurrency:
    def __init__(self, load_url, names_url, api_key, timeout, db, model):
        self.api_key = api_key
        self.timeout = timeout
        self.db = db.get_db()
        self.model = model
        self.load_url = load_url
        self.names_url = names_url

    async def load_all_currencies(self):
        self.db.query(self.model).delete()
        self.db.commit()
        headers = {"apikey": self.api_key}
        names = await self.get_names()
        rates = (json.loads((requests.get(url=self.load_url, headers=headers, timeout=self.timeout)).text))["rates"]
        for code, rate in rates.items():
            model = self.model(name=names[code], code=code, rate=rate)
            self.db.add(model)
        self.db.commit()

    async def get_names(self):
        headers = {"apikey": self.api_key}
        return (json.loads((requests.get(url=self.names_url, headers=headers, timeout=self.timeout)).text))["symbols"]


class ConvertCurrency:
    def __init__(self, load_currency: LoadCurrency, db, model):
        self.load_currency = load_currency
        self.db = db.get_db()
        self.model = model

    async def convert_currency(self, schema):
        await self.load_currency.load_all_currencies()
        amount = abs(schema.amount)
        rates = dict([item for item in self.db.query(self.model.rate, self.model.code).filter(
            or_(self.model.code == schema.source, self.model.code == schema.target)).all()])
        rates = dict(zip(rates.values(), rates.keys()))

        if amount and schema.source in [*rates.keys()] and schema.target in [*rates.keys()]:
            return amount * ((amount * rates[schema.target]) / (amount * rates[schema.source]))
        raise HTTPException(status_code=422, detail="Amount can't be zero!") if not amount\
            else HTTPException(status_code=404, detail="Currency not found!")


class GetAllCurrency:
    def __init__(self, load_currency: LoadCurrency, schema, db, model):
        self.load_currency = load_currency
        self.db = db.get_db()
        self.model = model
        self.schema = schema

    async def get_all_currency_rates(self):
        await self.load_currency.load_all_currencies()
        result = []
        all_currency_rates = self.db.query(self.model).all()
        for currency_rate in all_currency_rates:
            result.append(self.schema(**currency_rate.__dict__))
        return result

