from config import DBConfig, API_KEY
from dependency_injector import containers, providers
from src.models import CurrencyConverter
from src.schemas import CurrencyConvertSchema, CurrencySchema
from src import manager


class CurrencyContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[".routes"])
    config = providers.Configuration()

    currency_convert_schema = CurrencyConvertSchema
    currency_schema = CurrencySchema
    model = CurrencyConverter

    db_url = f"postgresql://{DBConfig.DB_USER}:{DBConfig.DB_PASS}@{DBConfig.DB_HOST}/{DBConfig.DB_NAME}"

    load_url = "https://api.apilayer.com/exchangerates_data/latest?&base=USD"
    names_url = "https://api.apilayer.com/exchangerates_data/symbols"
    api_key = API_KEY
    timeout = 10

    db = providers.Factory(
        manager.Database,
        db_url,
    )

    load_currency = providers.Factory(
        manager.LoadCurrency,
        load_url,
        names_url,
        api_key,
        timeout,
        db,
        model,
    )

    get_all_currency = providers.Factory(
        manager.GetAllCurrency,
        load_currency,
        currency_schema,
        db,
        model,
    )

    convert_currency = providers.Factory(
        manager.ConvertCurrency,
        load_currency,
        db,
        model,
    )
