import json

def view_lmap(ldata):
    with open(ldata) as f:
        f_data = json.load(f)
        str_data = ""
        for discip,value in f_data.items():
            str_data += f"Дисциплина {discip}\n\t"

            for level,programm in value.items():
                str_data += f"Уровень {level.replace('level_','')}\n\t\t"
                str_data += f"Предметы {" | ".join(programm)}\n\t"
        print(str_data)