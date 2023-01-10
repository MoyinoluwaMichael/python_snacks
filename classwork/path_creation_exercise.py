# import pathlib
#
# file_path = pathlib.Path.home() / "my_folder"
# file_path.mkdir(exist_ok=True)
# new_file = file_path / "my_file.txt"
# new_file.touch(exist_ok=True)
#
# print(file_path.exists())
# print(new_file.name)
# print(new_file.parent.name)

import pathlib

file_path = pathlib.Path.cwd()
original_path = file_path.parent / "self_assessment" / "diamond_printing_program.py"
original_path.touch()

