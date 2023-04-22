# Currency Converter Setup
0. terminal > pip install requirements.txt
1. Проставить переменные в .env (использовать базу postgresql, API_KEY брать с https://exchangeratesapi.io/)
2. terminal > alembic upgrade head
3. Запустить приложение командой 'uvicorn main:app --reload' и пользоваться


# Получение всех курсов валют:
<img height="400" src="https://github.com/Lufa1u/Currency_Converter/blob/main/images/Screenshot_2.png?raw=true" width="600"/>

# Конвертирование валют:
<img height="400" src="https://github.com/Lufa1u/Currency_Converter/blob/main/images/Screenshot_1.png?raw=true" width="600"/>