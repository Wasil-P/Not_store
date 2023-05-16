from sqlalchemy import create_engine, select, exc, update as sqlalchemy_update
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase




class MetaSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SessionManager(metaclass=MetaSingleton):
    def __init__(self):
            self._engine = None
            self._session = None

    def init_engine(self, dsn: str):
        self._engine = create_engine(dsn)
        self._session = sessionmaker(
            bind=self._engine,
            expire_on_commit=False,
        )

    def __call__(self, *args, **kwargs):
        return self._session(*args, **kwargs)

    def __getattr__(self, item):
        return getattr(self._session, item)

    def create_tables(self):
        Base.metadata.create_all(bind=self._engine)


session = SessionManager()


class Base(DeclarativeBase):

    @classmethod
    def get(cls, **kwargs):

        params = [getattr(cls, key) == val for key, val in kwargs.items()]
        query = select(cls).where(*params)

        try:
            with session() as conn:
                results = conn.execute(query)
                (res,) = results.one()
                return res
        except exc.NoResultFound:
            return None

    @classmethod
    def create(cls, **kwargs):

        obj = cls(**kwargs)
        with session() as conn:
            conn.add(obj)
            conn.commit()
        return obj

    def update(self, **kwargs) -> None:

        with session() as conn:
            conn.execute(
                sqlalchemy_update(self.__class__)
                .where(self.__class__.id == self.id)
                .values(**kwargs)
            )
            conn.commit()

    @classmethod
    def filter(cls, **kwargs):

        params = [getattr(cls, key) == val for key, val in kwargs.items()]
        query = select(cls).where(*params)
        try:
            with session() as conn:
                results = conn.execute(query)
                return results.scalars().all()
        except exc.NoResultFound:
            return []

    @classmethod
    def all(cls):

        with session() as conn:
            results = conn.execute(select(cls))
            return results.scalars().all()