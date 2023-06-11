import os

def rename_files(folder_path):
    file_list = os.listdir(folder_path)

    file_list.sort()

    for index, filename in enumerate(file_list):
        name, extension = os.path.splitext(filename)

        new_filename = f"{index + 1}{extension}"

        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_filename)

        os.rename(old_path, new_path)

        print(f"Renamed {filename} to {new_filename}")

folder_path = "./data"

rename_files(folder_path)
