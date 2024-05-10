from view_lmap import view_lmap
from del_elem_lmap import del_elem_lmap
from add_elem_lmap import add_elem_lmap

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
                ret_elem = del_elem_lmap(self.file_data,del_elem)
                print(f"{del_elem} {'был удален!!!' if ret_elem else 'не найден!!!'}")
            elif self.user_com == '3':
                pass
            elif self.user_com == '4':
                elem = self._create_add_elem()
                print(add_elem_lmap(self.file_data, elem))
            else:
                print('!!!Нет такой команды (команды = q,1,2,3)!!!')

    def _create_add_elem(self):
        elem_info = {}
        elem_info['prog'] = input("Введите предмет который хотите добавить => ")
        elem_info['level'] = f"level_{input("Введите его уровень => ")}"
        elem_info['dic'] = input("Введите дисциплину => ")
        return elem_info

if __name__ == "__main__":
    lmap = LearningMap('learning_data.json')
    lmap.run()