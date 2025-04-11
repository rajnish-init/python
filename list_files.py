import os

folders = input("provide provide list of folders names with spaces in between:").split()

for folder in folders:

    try:
        files = os.listdir(folder)
        print(f"Files in {folder} : {files}")
    except FileNotFoundError:
        print(f"Folder {folder} does not exist.")
        continue

    for file in files:
        print(file)