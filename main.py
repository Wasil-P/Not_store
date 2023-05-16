# from data_base import db
# from data_base.db import Base
from data_base.db import session
# from models.all_models import Products
from data_base.db import SessionManager
from storage.menu import UserMenu
from storage.service import ShopService
from storage.memory_storage import MemoryStorage

if __name__ == "__main__":

    session.init_engine("postgresql://postgres:postgres@localhost:5432/not store")
    session.create_tables()


session2 = SessionManager()
session3 = SessionManager()

print(session2 is session)
print(session2 is session3)

# s_products = Products(name="silver pen", cost=10, count=100)
# p_products = Products(name="platinum pen", cost=20, count=12)
# g_products = Products(name="golden pen", cost=40, count=2)
# session.add(s_products)
# session.add(p_products)
# session.add(g_products)
# session.commit()


#  Добавить пункт меню (Закрыть программу)
#  Добавить пункт меню (Сменить пользователя)

memory_storage = MemoryStorage()

menu = UserMenu(storage=memory_storage)
service = ShopService(storage=memory_storage)

menu.add_menu_category(
    name="Войти",
    callback=service.login,
    login_required=False,
)
menu.add_menu_category(
    name="Зарегистрироваться",
    callback=service.register,
    login_required=False,
)
menu.add_menu_category(
    name="Тикет",
    callback=service.submit_ticket,
    login_required=True,
)
menu.add_menu_category(
    name="Купить",
    callback=service.buy_product,
    login_required=True,
)
menu.add_menu_category(
    name="Профиль",
    callback=service.profile,
    login_required=True,
)
menu.add_menu_category(
    name="Товары",
    callback=service.display_products,
    login_required=False,
)
menu.add_menu_category(
    name="Сменить пользователя",
    callback=service.login,
    login_required=True,
)
menu.add_menu_category(
    name="Закрыть программу",
    callback=service.exit_now,
    login_required=False,
)
while True:
    menu.display_categories()
    menu.handler()