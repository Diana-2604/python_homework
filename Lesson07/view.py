def show_menu() -> int:
    print("\n Выберите необходимое действие:\n"
        "1. Отобразить весь справочник\n"
        "2. Найти абонента по имени\n"
        "3. Найти абонента по номеру телефона\n"
        "4. Добавить абонента в справочник\n"
        "5. Сохранить справочник в текстовом формате\n"
        "6. Закончить работу")
    choice = int(input())
    return choice

def print_result(data: list) -> list:
    for el in data:
        s = ''
        for k, v in el.items(): 
            s += f'{k}: {v}\n' # key : value
        print(s)

def get_search_name() -> str:
    return input("Введите имя для поиска: ")

def get_search_number() -> str:
    return input("Введите номер телефона для поиска: ")

def get_new_user() -> str:
    id = input("Введите порядковый номер абонента: ")
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    number = input("Введите номер телефона: ")
    return f'{id},{name},{surname},{number}'

def get_file_name() -> str:
    return input("Введите название файла для сохранения: ")