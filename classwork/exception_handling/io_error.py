from pathlib import Path

try:
    file_name = open("path", "w")
    file_name.write("Iba oluwo n koko tilu koko")
except IOError:
    print("Cannot write to a closed file")
else:
    file_name.close()
    print("Successful")
finally:
    print("Sibe sibe, mo japa")


# try:
#     file_name = open(Path.cwd())