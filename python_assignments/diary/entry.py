import datetime
from python_assignments.diary.date_time import DateTime


class Entry:
    def __init__(self, title: str, body: str, i_d: int):
        self.title: str = title
        self.body: str = body
        self.i_d: int = i_d
        self.date_and_time = DateTime()

    def __str__(self) -> str:
        return f"""
        ========================================================================================================================
        TITLE: {self.title}
        ID: {self.i_d}{self.date_and_time.__str__()}
        ========================================================================================================================
        Body:
        {self.body}
        ========================================================================================================================
        """

    def get_entry_i_d(self) -> int:
        return self.i_d

    def edit_body(self, entry_body) -> None:
        self.body = entry_body
