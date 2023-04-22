from fastapi import FastAPI
from src import routes


app = FastAPI()


app.include_router(routes.router, prefix="/currency_converter", tags=["CURRENCY_CONVERTER"])
