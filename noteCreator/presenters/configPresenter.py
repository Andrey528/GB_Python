from models.notesHandler import NotesHandler
from views.consoleView import ConsoleView
from models.noteClass import Note
from models.csvWorker import CsvWorker

class ConfigPresenter:
    def __init__(self):
        self._notes = NotesHandler()
        self._view = ConsoleView()
        self._csvWorker = CsvWorker()

    def process_input(self, choose):
        if choose == 1:
            self._notes.add_note(Note(len(self._notes.get_notes()),
                                self._view.get_string_user_input("Введите заголовок\n"),
                                self._view.get_string_user_input("Введите тело\n")))
        elif choose == 2:
            self._notes.update_note(self._view.get_int_user_input("Введите индекс редактируемой заметки\n"),
                                    self._view.menu_to_update_note(),
                                    self._view.get_string_user_input("Введите новое значение поля\n"))
        elif choose == 3:
            self._notes.delete_note(self._view.get_int_user_input("Введите индекс удаляемой заметки\n"))
        elif choose == 4:
            print(self._notes.get_note_by_index(self._view.get_int_user_input("Введите индекс просматривоемой заметки\n")))
        elif choose == 5:
            print(*self._notes.get_notes(), sep='\n')
        elif choose == 6:
            self._csvWorker.save_to_csv(self._notes.get_notes())
        elif choose == 7:
            data = self._csvWorker.read_csv()
            self._view.show_message(data)

    def start_program(self):
        while(True):
            choose = self._view.show_menu()
            if choose == 8:
                break
            if (choose < 1 or choose > 8):
                self._view.show_message("Ошибка. Выбор должен быть от 1 до 8")
                continue
            self.process_input(choose)