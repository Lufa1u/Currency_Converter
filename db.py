from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config import DBConfig


def get_url():
    user = DBConfig.DB_USER
    password = DBConfig.DB_PASS
    host = DBConfig.DB_HOST
    name = DBConfig.DB_NAME
    return f"postgresql://{user}:{password}@{host}/{name}"


def get_db():
    url = get_url()
    engine = create_engine(url)
    SessionClass = sessionmaker(bind=engine)
    return SessionClass()
