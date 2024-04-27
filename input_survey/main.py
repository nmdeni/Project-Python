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
    new_user = {
        # 'user_id': '',
        'user_name': '',
        'user_lastname': '',
        'user_age': '',
        'user_status': '',
        'user_work': '',
        'user_info': ''
    }

    # ЗДЕСЬ РАБОТА С ID

    for key,val in new_user.items():
            if key == 'user_name' or key == 'user_lastname':
                new_user[key] = input(f"Введите {key} => ").title()
            else:
                new_user[key] = input(f"Введите {key} => ")

    print(f"Данные про {new_user['user_name']} записаны!\nНажмите enter!")
    input()

    return new_user
def rem_user(user):
    pass
    """
        сюда передается от пользователя id юзера которого надо удалить
        сообщается о заисимостях и о том что это не вернуть
        удаляется и возвращается имя удаленного юзера
    """
    return user
def edit_user():
    pass

start_prog = True
command = [
    "1 - Вывести все древо",
    "2 - Вывести инфо человека",
    "3 - Добавить человека",
    "4 - Удалить человека",
    "5 - Редактировать информацию",
    "q - Выход"
]

while start_prog:
    print("\n".join(command) + "\n")

    user_com = input('Введите команду => ')
    if user_com.lower() == "q":
        break
    elif user_com == "3":
        add_user()
        # ЗДЕСЬ ЗАПИСЬ В БД
    elif user_com == "4":
        print(f"{rem_user(input("Кого хотите удалить => "))} был удален!\n Нажмиете enter!")
        input()