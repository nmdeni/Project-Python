def tree_view():
    pass
    """
        эта функция должна обращаться к БД 
        получать от туда информацию о ВСЕХ участников дерева
        СКОРЕЕ всего создавать объект в котором буду дочки в формате
        имя, фамилия, пренодлежность к дочери/сыну и пренодлежность ко мне
        далее выводить это все на вьюшку
    """
def user_view():
    pass
    """
        Эта функция должна обращаться к БД
        получать от туда информацию о КОНКРЕТНОМ запрашиваемом юзере
        и СКОРЕЕ всего создавать ловарь с информацией 
        и выводить его на вьюшку
    """
def add_user():
    pass
    
def rem_user():
    pass
def edit_user():
    pass

user_date = {
    'user_id':'',
    'user_name':'',
    'user_lastname':'',
    'user_age':'',
    'user_status':'', #переделать под зависимость (пример = мама => дочери)
    'user_work':'',
    'user_info':''
}

start_prog = True

# for key,val in user_date.items():
#     if key == 'user_id':
#         user_date[key] = (1)
#     elif key == 'user_name' or key == 'user_lastname':
#         user_date[key] = input('Введите ' + str(key) + ' -> ').title()
#     else:
#         user_date[key] = input('Введите ' + str(key) + ' -> ')
#
# print(f"*** ИНФОРМАЦИЯ О {user_date['user_name']} ***")
# for key,val in user_date.items():
#     print(f"{key.replace('user_','').title()} => {val}")

while start_prog:
    command = [
        "1 - Вывести все древо",
        "2 - Вывести инфо человека",
        "3 - Добавить человека",
        "4 - Удалить человека",
        "5 - Редактировать информацию",
        "q - Выход"
    ]
    print("\n".join(command) + "\n")

    user_com = input('Введите команду => ')
    if user_com.lower() == "q":
        break