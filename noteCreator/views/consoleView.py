from models.noteClass import Note
from models.notesHandler import NotesHandler

class ConsoleView:
    def show_menu(self):
        user_input = self.get_int_user_input('''Выберите индекс пункта меню:
              1. Добавить заметку;
              2. Редактировать заметку;
              3. Удалить заметку;
              4. Показать заметку по индексу;
              5. Показать заметки;
              6. Сохранить заметки в CSV;
              7. Прочитать заметки из CSV;
              8. Выйти\n''')
        return user_input

    def get_int_user_input(self, message):
        user_input = int(input(message))
        return user_input

    def get_string_user_input(self, message):
        user_input = input(message)
        return user_input

    def show_message(self, message):
        print(message)

    def menu_to_update_note(self):
        choice = self.get_int_user_input('''Какое поле требуется отредактировать:
                                        1. Title;
                                        2. Body.\n''')
        if (choice < 1 or choice > 2):
            self.show_message("Ошибка - такого пункта в меню нет")
            return
        return choice