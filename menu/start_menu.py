from models.users import Users
from continue_menu import start_after_authorization
import main

greetings_start = print('== Добро пожаловать в "Не магазин"!\n'
                  'Здесь вы можете обменивать тикеты для того, чтобы приобретать товары.\n'
                  'Для взаимодействия используйте команды:\n'
                  '> Товары\n'
                  '> Зарегистрироваться\n'
                  '> Войти\n')


def begin_menu_navigation():

    while True:
        command_start = input("Введите команду: ")
        if command_start != "Товары" and command_start != "Зарегистрироваться" and command_start != "Войти":
            print("Вы ввели недопустимую команду. Повторите ввод.")
        elif command_start == "Товары":
            print_table_prod()
        elif command_start == "Зарегистрироваться":
            input_username = input("Введите логин: ")
            if Users.is_exists(input_username) == False:
                print("Такой пользователь уже существует")
            else:
                input_password = input("Введите пароль: ")
                new_user = Users(username=input_username, password=input_password)
                start_after_authorization()
        elif command_start == "Войти":
            start_after_authorization()


id = "ID"; cost = "Стоимость"; count = "Количество"; _name = "Название"
def print_table_prod():
    print(f"{id:<15}{cost:<15}{count:<15}{_name:<15}")
    print(f"{main.s_products.id:<15}{main.s_products.cost:<15}{main.s_products.count:<15}{main.s_products.name:<15}")
    print(f"{main.p_products.id:<15}{main.p_products.cost:<15}{main.p_products.count:<15}{main.p_products.name:<15}")
    print(f"{main.g_products.id:<15}{main.g_products.cost:<15}{main.g_products.count:<15}{main.g_products.name:<15}")


begin = begin_menu_navigation()


