def start():
    user_com = ''
    menu = [
        'q - Выход',
        '1 - Поменять статус предмета/уровень',
        '2 - Удалить предмет/уровень',
        '3 - Редактировать предмет/уровень'
    ]
    for i in menu:
        print(i)

    while user_com.lower() != 'q':
        user_com = input('Введите команду => ')
        if user_com not in menu:
            print('!!!Нет такой команды (команды = q,1,2,3)!!!')

if __name__ == "__main__":
    start()