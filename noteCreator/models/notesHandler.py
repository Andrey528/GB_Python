class NotesHandler:
    def __init__(self):
        self._notesList = []

    def add_note(self, note):
        self._notesList.append(note)

    def get_note_by_index(self, index):
        return self._notesList[index]

    def get_notes(self):
        return self._notesList

    def delete_note(self, index):
        if len(self._notesList) != 0:
            self._notesList.pop(index)
        else: print("Can't remove item")

    def update_note(self, noteIndex, fieldChoice, fieldText):
        note = self.get_note_by_index(noteIndex)
        if fieldChoice == 1:
            note.set_title(fieldText)
            note.update_date()
        elif fieldChoice == 2:
            note.set_body(fieldText)
            note.update_date()