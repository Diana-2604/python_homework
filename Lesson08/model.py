def write_txt(filename: str, data: list):
    with open(filename, 'w', encoding= 'utf-8') as fout:
        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n') #[:-1] отрезать запятую в конце

def add_csv(filename: str, data: list):
    with open(filename, 'a', encoding= 'utf-8') as fout:
        for i in range(len(data)-1, len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')

def write_csv(filename: str, data: list):
    with open(filename, 'w', encoding= 'utf-8') as fout:
        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')

def read_csv(filename: str) -> list:
    data = []
    fields = ["ID", "Имя", "Фамилия", "Класс", "Успеваемость"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data

def find_by_surname(data: list, surname: str) -> str:
    for el in data:
        if el.get("Фамилия") == surname:
            return el.get("Класс")
    return "Такой ученик не найден"

def find_by_room(data: list, room: str) -> str:
    s = ''
    for el in data:
        if el.get("Класс") == room:
            for k, v in el.items(): 
                s += f'{k}: {v}\n' # key : value
    return(s)
    

def find_by_score(data: list, score: str) -> str:
    s = ''
    for el in data:
        if el.get("Успеваемость") == score:
            for k, v in el.items(): 
                s += f'{k}: {v}\n' # key : value
    return(s)
    

def add_pupil(data: list, pupil_data: str) -> list:
    fields = ["ID", "Имя", "Фамилия", "Класс", "Успеваемость"]
    new_pupil = dict(zip(fields, pupil_data.strip().split(',')))
    data.append(new_pupil)
    return data

def remove_pupil(data: list, pupil_id: str) -> list:
    for el in data:
        if el.get("ID") == pupil_id:
            index = data.index(el)
            data.remove(data[index])
    return data
