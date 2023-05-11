from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = None
Session = sessionmaker()


def configure_engine():
    global engine
    if engine is None:
        engine = create_engine("postgresql://postgres:postgres@localhost:5432/not store")
        Session.configure(bind=engine)
