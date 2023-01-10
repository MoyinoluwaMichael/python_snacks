from pathlib import Path

# 1
new_folder = Path.home() / "my_folder"
new_folder.mkdir(exist_ok=True)

# 2
new_files = [
    new_folder / "file1.txt",
    new_folder / "file2.txt",
    new_folder / "image1.png"
]
for file in new_files:
    file.touch(exist_ok=True)

# 3
image_folder = new_folder / "images"
image_folder.mkdir(exist_ok=True)
source = new_folder / "image1.png"
destination = image_folder / "image1.png"
source.replace(destination)

# 4
file1_file = new_folder / "file1.txt"
file1_file.unlink(missing_ok=True)

# 5
for file in new_folder.rglob("*.png"):
    file.unlink(missing_ok=True)
file2_file = new_folder / "file2.txt"
file2_file.unlink()
image_folder.rmdir()
new_folder.rmdir()

