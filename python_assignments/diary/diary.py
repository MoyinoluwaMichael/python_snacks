from python_assignments.diary.entry import Entry


class Diary:

    def __init__(self):
        self.__entries: list[Entry] = []
        self.__i_d_count = 1
        self.opening_count: int = 0

    def create_entry(self, title: str, body: str) -> None:
        self.opening_count = 1
        self.__entries.append(Entry(title, body, self.__i_d_count))
        self.__i_d_count += 1

    def get_number_of_entries_created(self) -> int:
        return len(self.__entries)

    def view_entry_at(self, i_d) -> str:
        return self.find_entry(i_d).__str__()

    def find_entry(self, i_d) -> Entry:
        for entry in self.__entries:
            print(entry.get_entry_i_d())
            if entry.get_entry_i_d() == i_d:
                return entry
        raise ValueError("Entry not found.")

    def delete_entry_at(self, i_d: int) -> None:
        self.__entries.remove(self.find_entry(i_d))

    def edit_entry_at(self, i_d, entry_body):
        self.find_entry(i_d).edit_body(entry_body)

