from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, func
from datetime import datetime
from data_base.db import Base


class Products(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    cost: Mapped[int]
    count: Mapped[int]
    _orders: Mapped[list["Orders"]] = relationship(back_populates="_products")


class DoesNotExist(Exception):
    pass


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    password: Mapped[str]
    points: Mapped[int] = mapped_column(default=0)
    _orders: Mapped[list["Orders"]] = relationship(back_populates="_users")
    _tickets: Mapped[list["Tickets"]] = relationship(back_populates="_users")

    @staticmethod
    def is_exists(username: str) -> bool:
        try:
            Users.get(username=username) is not None
        except DoesNotExist:
            return True
        else:
            return False



class Tickets(Base):
    __tablename__ = "tickets"

    id: Mapped[int] = mapped_column(primary_key=True)
    uuid: Mapped[int]
    available: Mapped[bool]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    _users: Mapped[list["Users"]] = relationship(back_populates="_tickets")


class Orders(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    _users: Mapped[list["Users"]] = relationship(back_populates="_orders")
    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'))
    _products: Mapped[list["Products"]] = relationship(back_populates="_orders")
    count: Mapped[int]
    order_datetime: Mapped[datetime] = mapped_column(server_default=func.CURRENT_TIMESTAMP())

