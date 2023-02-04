import pickle

from python_assignments.diary.diary import Diary

diary = Diary()
try:
    file = open("diary-file.pkl", "rb")
    diary = pickle.load(file)
    file.close()
except FileNotFoundError:
    print()


def collect_input(prompt: str):
    try:
        inp = input(prompt)
    except IndexError:
        print("Invalid input")
    else:
        if inp == "":
            print("Invalid input")
            go_to_main_menu()
        else:
            return inp


def create_entry():
    entry_title = collect_input("Enter the title of your Entry\n")
    entry_body = collect_input("Enter the body of your Entry\n")
    try:
        diary.create_entry(entry_title, entry_body)
    except ValueError as e:
        print(e.__str__())
    finally:
        go_to_main_menu()


def view_entry():
    id_number = collect_input("Enter Entry ID number")
    try:
        print(diary.view_entry_at(int(id_number)))
    except ValueError as e:
        print(e.__str__())
    finally:
        go_to_main_menu()


def delete_entry():
    id_number = collect_input("Enter Entry ID number")
    try:
        diary.delete_entry_at(int(id_number))
    except ValueError as e:
        print(e.__str__())
    else:
        print("Entry specified has been deleted.")
    finally:
        go_to_main_menu()


def check_number_of_entries_created():
    try:
        print(diary.get_number_of_entries_created())
    except ValueError as e:
        print(e.__str__())
    finally:
        go_to_main_menu()


def edit_entry():
    id_number = collect_input("Enter Entry ID number")
    try:
        print(diary.view_entry_at(int(id_number)))
    except ValueError as e:
        print(e.__str__())
    else:
        new_entry_body = collect_input("Enter the new body of your entry")
        try:
            diary.edit_entry_at(int(id_number), new_entry_body)
        except ValueError as e:
            print(e.__str__())
        else:
            print("Entry edited successfully")
    finally:
        go_to_main_menu()


def exit_app():
    print("Thank you for using our app")
    with open("diary-file.pkl", "wb") as saved_file:
        pickle.dump(diary, saved_file)
        saved_file.close()


def go_to_main_menu():
    main_menu: str = """
                1 -> Create Entry
                2 -> View Entry
                3 -> Delete Entry
                4 -> Check Number of Entries Created
                5 -> Edit Entry
                6 -> Exit Diary
                """
    user_input = collect_input(main_menu)
    if user_input.__getitem__(0) == '1':
        create_entry()
    elif user_input.__getitem__(0) == '2':
        view_entry()
    elif user_input.__getitem__(0) == '3':
        delete_entry()
    elif user_input.__getitem__(0) == '4':
        check_number_of_entries_created()
    elif user_input.__getitem__(0) == '5':
        edit_entry()
    elif user_input.__getitem__(0) == '6':
        exit_app()
    else:
        go_to_main_menu()


class DiaryMain:
    if __name__ == '__main__':
        go_to_main_menu()
