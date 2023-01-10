from pathlib import Path

practice_folder = Path.home() / "practice_files_folder"
practice_folder.mkdir(exist_ok=True)

documents_folder = practice_folder / "documents"
documents_folder.mkdir(exist_ok=True)
sub_folder = documents_folder / "sub_folder"
sub_folder.mkdir(exist_ok=True)

image_files = [
    documents_folder / "image1.png",
    documents_folder / "image2.gif",
    documents_folder / "image3.png",
    documents_folder / "image4.jpg",
]
for file in image_files:
    file.touch(exist_ok=True)

image_folder = practice_folder / "images"
image_folder.mkdir(exist_ok=True)

source = documents_folder / "image1.png"
destination = image_folder / "image1.png"
source.replace(destination)

source = documents_folder / "image2.gif"
destination = image_folder / "image2.gif"
source.replace(destination)

source = documents_folder / "image3.png"
destination = image_folder / "image3.png"
source.replace(destination)

source = documents_folder / "image4.jpg"
destination = image_folder / "image4.jpg"
source.replace(destination)

