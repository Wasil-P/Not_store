from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base
from orders import Orders
from tickets import Tickets

class DoesNotExist(Exception):
    pass


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    password: Mapped[str]
    points: Mapped[int] = mapped_column(default=None)
    _orders: Mapped[list["Orders"]] = relationship(back_populates="_users")
    _tickets: Mapped[list["Tickets"]] = relationship(back_populates="_users")

    @staticmethod
    def is_exists(username: str) -> bool:
        try:
            Users.get(Users.username == username)
        except DoesNotExist:
            return False
        else:
            return True

    @classmethod
    def get(cls, param):
        pass