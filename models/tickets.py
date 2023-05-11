from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from models import Base
from users import Users

class Tickets(Base):
    __tablename__ = "tickets"

    id: Mapped[int] = mapped_column(primary_key=True)
    uuid: Mapped[int]
    available: Mapped[bool]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    _users: Mapped[list["Users"]] = relationship(back_populates="_tickets")