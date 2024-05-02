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