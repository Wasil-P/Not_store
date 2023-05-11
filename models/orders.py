from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, func
from datetime import datetime
from models import Base
from users import Users
from products import Products


class Orders(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    _users: Mapped[list["Users"]] = relationship(back_populates="_orders")
    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'))
    _products: Mapped[list["Products"]] = relationship(back_populates="_orders")
    count: Mapped[int]
    order_datetime: Mapped[datetime] = mapped_column(server_default=func.CURRENT_TIMESTAMP())

