import uuid
import main


new_uuid = str(uuid.uuid4())

def start_after_authorization():
    greetings_start = print('Для взаимодействия используйте команды:\n'
                            '> Товары\n'
                            '> Купить\n'
                            '> Профиль\n'
                            '> Тикет')
    while True:
        command_continue = input("Введите команду: ")
        if command_continue != "Товары" and \
                command_continue != "Купить" and \
                command_continue != "Профиль" and \
                command_continue != "Тикет":
            print("Вы ввели недопустимую команду. Повторите ввод.")
        elif command_continue == "Товары":
            print_table_prod()
        elif command_continue == "Купить":
            print("купить")
        elif command_continue == "Профиль":
            print("Профиль")
        elif command_continue == "Тикет":
            print("Тикет")


id = "ID"; cost = "Стоимость"; count = "Количество"; _name = "Название"
def print_table_prod():
    print(f"{id:<15}{cost:<15}{count:<15}{_name:<15}")
    print(
        f"{main.s_products.id:<15}{main.s_products.cost:<15}{main.s_products.count:<15}{main.s_products.name:<15}")
    print(
        f"{main.p_products.id:<15}{main.p_products.cost:<15}{main.p_products.count:<15}{main.p_products.name:<15}")
    print(
        f"{main.g_products.id:<15}{main.g_products.cost:<15}{main.g_products.count:<15}{main.g_products.name:<15}")

