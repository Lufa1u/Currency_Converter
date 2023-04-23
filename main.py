from fastapi import FastAPI
from src import routes
from src.containers import CurrencyContainer


def create_app():
    container = CurrencyContainer()
    app = FastAPI()
    app.container = container
    app.include_router(routes.router, prefix="/currency_converter", tags=["CURRENCY_CONVERTER"])
    return app


app = create_app()
