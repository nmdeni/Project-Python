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

        return str_data

# def del_elem_lmap(ldata):
#     del_elem = input('Какой предмет удалить => ')
#     with open(ldata,encoding='utf-8') as f:
#         f_data = json.load(f)
#         for dic,levels in f_data.items():
#             for level,program in levels.items():
#                 if del_elem in program:
#                     program.remove(del_elem)
#                     with open(ldata,'w',encoding='utf-8') as f:
#                         json.dump(f_data,f)
#                     return del_elem
#
# def add_elem_lmap(ldata):
#     """Функция для добавления эелментов в карту"""
#
#     elem_param = []
#     user_elem = input("Введите предмет который хотите добавить => ")
#
#     while user_elem != 'q':
#         # Собираем параметры для элемента
#         if len(elem_param) == 0:
#             elem_param.append(user_elem)
#         elif len(elem_param) < 2:
#             elem_param.append(input("Введите его уровень => "))
#         elif len(elem_param) < 3:
#             elem_param.append(input("Введите дисциплину => "))
#             with open(ldata,encoding='utf-8') as f:
#                 f_data = json.load(f)
#                 if elem_param[-1] not in f_data.keys():
#                     dic = elem_param.pop(-1)
#                     level = f"level_{elem_param.pop(-1)}"
#                     prog = [elem_param.pop(-1)]
#                     f_data[dic] = {level:prog}
#                     print(f_data[dic])
