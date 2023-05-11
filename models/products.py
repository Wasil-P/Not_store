from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base
from orders import Orders


class Products(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    cost: Mapped[int]
    count: Mapped[int]
    _orders: Mapped[list["Orders"]] = relationship(back_populates="_products")