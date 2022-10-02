def show_menu() -> int:
    print("\n Выберите необходимое действие:\n"
        "1. Найти ученика по фамилии\n"
        "2. Сделать выборку учеников по классу\n"
        "3. Сделать выборку учеников по успеваемости\n"
        "4. Добавить ученика\n"
        "5. Удалить ученика\n"
        "6. Экспортировать данные в текстовом формате\n"
        "7. Закончить работу\n")
    choice = int(input())
    return choice

def get_search_surname() -> str:
    return input("Введите фамилию для поиска: ")

def get_search_room() -> str:
    return input("Введите название класса для поиска: ")

def get_search_score() -> str:
    return input("Введите успеваемость для поиска: ")

def get_new_pupil() -> str:
    id = input("Введите порядковый номер ученика: ")
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    room = input("Введите название класса: ")
    score = input("Введите успеваемость: ")
    return f'{id},{name},{surname},{room},{score}'

def get_remove_id() -> str:
    return input("Введите данные ученика для удаления: ")

def get_file_name() -> str:
    return input("Введите название файла для экспорта данных: ")