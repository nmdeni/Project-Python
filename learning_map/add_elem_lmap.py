import json

def add_elem_lmap(data,elem):
    """Функция для добавления эелментов в карту"""
    with open(data, encoding='utf-8') as f:
        f_data = json.load(f)
        # Если дисциплина новая
        if elem['dic'] not in f_data.keys():
            dic = elem['dic']
            level = elem['level']
            prog = elem['prog']
            f_data[dic] = {level: [prog]}
            return f_data
        # Если дисциплина есть
        elif elem['dic'] in f_data.keys():
            # Если есть левел
            if elem['level'] in f_data[elem['dic']].keys():
                # Если есть программа
                if elem['prog'] in f_data[elem['dic']][elem['level']]:
                    return "Элемент существует!!!"
                else:
                    f_data[elem['dic']][elem['level']].append(elem['prog'])
                    return f_data