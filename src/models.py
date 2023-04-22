from sqlalchemy import Column, String, Integer, FLOAT
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class CurrencyConverter(Base):
    __tablename__ = 'currency_converter'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String, nullable=False)
    code = Column(String, nullable=False)
    rate = Column(FLOAT, nullable=False)

