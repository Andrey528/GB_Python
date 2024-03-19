from datetime import datetime

class Note:
    def __init__(self, noteId, title, body):
        self._noteId = noteId
        self._title = title
        self._body = body
        self._date = datetime.now()

    def __str__(self):
        return f'{self._noteId}, {self._title}, {self._body}, {self._date}'

    def set_title(self, title):
        self._title = title

    def set_title(self, body):
        self._title = body

    def update_date(self):
        self._date = datetime.now()

    def get_noteId(self):
        return self._noteId

    def get_title(self):
        return self._title

    def get_body(self):
        return self._body

    def get_date(self):
        return self._date