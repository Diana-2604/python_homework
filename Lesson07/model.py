def write_txt(filename: str, data: list):
    with open(filename, 'w', encoding= 'utf-8') as fout:
        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n') #[:-1] отрезать запятую в конце

def write_csv(filename: str, data: list):
    with open(filename, 'a', encoding= 'utf-8') as fout:
        for i in range(len(data)-1, len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')

def read_csv(filename: str) -> list:
    data = []
    fields = ["ID", "Имя", "Фамилия", "Телефон"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data

def find_by_name(data: list, name: str) -> str:
    for el in data:
        if el.get("Имя") == name:
            return el.get("Телефон")
    return "Такой абонент не найден"

def find_by_number(data: list, number: str) -> str:
    for el in data:
        if el.get("Телефон") == number:
            return f'{el.get("Имя")}, {el.get("Фамилия")}'
    return "Абонент с таким номером не найден"

def add_user(data: list, user_data: str) -> str:
    fields = ["ID", "Имя", "Фамилия", "Телефон"]
    new_user = dict(zip(fields, user_data.strip().split(',')))
    data.append(new_user)
    return data