import lmap

def start():
    user_com = ''
    learn_data = 'learning_data.json'
    menu = [
        'q - Выход',
        '1 - Поменять статус предмета/уровень',
        '2 - Удалить предмет/уровень',
        '3 - Редактировать предмет/уровень'
    ]

    #ВЫВОД КАРТА
    lmap.view_lmap(learn_data)
    for i in menu:
        print(i)

    while user_com.lower() != 'q':
        user_com = input('Введите команду => ')
        if user_com == "q":
            print("Завершение программы...")
        elif user_com == '1':
            pass
        elif user_com == '2':
            del_elem = lmap.del_elem_lmap(learn_data)
            print(f"{del_elem} был удален!!!")
        elif user_com == '3':
            pass
        else:
            print('!!!Нет такой команды (команды = q,1,2,3)!!!')

if __name__ == "__main__":
    start()