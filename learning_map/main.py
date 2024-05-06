from view_lmap import view_lmap
from del_elem_lmap import del_elem_lmap

class LearningMap():
    def __init__(self, file_name):
        self.file_data = file_name
        self.user_com = ''
        self.menu = [
            'q - Выход',
            '1 - Поменять статус предмета',
            '2 - Удалить предмет',
            '3 - Редактировать предмет',
            '4 - Добавить предмет'
        ]

    def run(self):
        # ВЫВОД КАРТА
        print(view_lmap(self.file_data))
        for i in self.menu:
            print(i)

        while self.user_com.lower() != 'q':
            self.user_com = input('Введите команду => ')
            if self.user_com == "q":
                print("Завершение программы...")
            elif self.user_com == '1':
                pass
            elif self.user_com == '2':
                del_elem = input('Какой предмет удалить => ')
                print(f"{del_elem_lmap(self.file_data,del_elem)} был удален!!!")
            elif self.user_com == '3':
                pass
            elif self.user_com == '4':
                pass
                # print(lmap.add_elem_lmap(learn_data))
            else:
                print('!!!Нет такой команды (команды = q,1,2,3)!!!')

if __name__ == "__main__":
    lmap = LearningMap('learning_data.json')
    lmap.run()