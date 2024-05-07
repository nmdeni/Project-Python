import json

def add_elem_lmap(data,elem):
    """Функция для добавления эелментов в карту"""
    with open(data, encoding='utf-8') as f:
        f_data = json.load(f)
        if elem[-1] not in f_data.keys():
            dic = elem.pop(-1)
            level = f"level_{elem.pop(-1)}"
            prog = [elem.pop(-1)]
            f_data[dic] = {level: prog}
            return f_data[dic]