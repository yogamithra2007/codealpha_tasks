import os
import shutil

source_folder = input("Enter source folder path: ")
destination_folder = input("Enter destination folder path: ")

files = os.listdir(source_folder)

for file in files:
    source_path = os.path.join(source_folder, file)
    destination_path = os.path.join(destination_folder, file)

    if os.path.isfile(source_path):
        shutil.copy(source_path, destination_path)
        print(f"Copied: {file}")

print("Task completed successfully!")
