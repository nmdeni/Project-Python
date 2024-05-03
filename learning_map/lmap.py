import json
import colorama
from colorama import Fore,Back,Style

def view_lmap(ldata):
    colorama.init()
    with open(ldata,encoding='utf-8') as f:
        f_data = json.load(f)
        str_data = ""
        for discip,value in f_data.items():
            str_data.strip()
            str_data += f"\r*** Дисциплина {discip.strip()} ***\n\t"

            for level,programm in value.items():
                str_data += f"Уровень {level.replace('level_','')}\n\t\t"

                str_data += "Предметы "
                for i in programm:
                    str_data += (f"{Fore.GREEN if "+" in i else ''}"
                                 f"{Fore.YELLOW if "#" in i else ''}"
                                 f"{i}{Style.RESET_ALL} | ")
                str_data +="\n\t"

        print(str_data)

def del_elem_lmap(ldata):
    del_elem = input('Какой предмет удалить => ')
    with open(ldata,encoding='utf-8') as f:
        f_data = json.load(f)
        for dic,levels in f_data.items():
            for level,program in levels.items():
                if del_elem in program:
                    program.remove(del_elem)
                    with open(ldata,'w',encoding='utf-8') as f:
                        json.dump(f_data,f)
                    return del_elem



