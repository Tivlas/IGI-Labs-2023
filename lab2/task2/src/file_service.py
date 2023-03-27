import json
from os import path, getcwd, makedirs
from storage import StorageEmulator


class FileService:
    save_and_read_all_directory = getcwd()

    @staticmethod
    def save(file_path):
        makedirs(path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as f:
            data = list(StorageEmulator.storage[StorageEmulator.cur_user])
            json.dump(data, f, ensure_ascii=False, indent=4)

    @staticmethod
    def load(file_path):
        if not path.isfile(file_path):
            raise ValueError("File does not exist")
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            StorageEmulator.storage[StorageEmulator.cur_user] |= set(data)

    @staticmethod
    def save_all():
        file_path = path.join(
            FileService.save_and_read_all_directory, "users_data.txt")
        makedirs(path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as f:
            data = {user: list(user_data)
                    for user, user_data in StorageEmulator.storage.items()}
            json.dump(data, f, ensure_ascii=False, indent=4)

    @staticmethod
    def load_all():
        file_path = path.join(
            FileService.save_and_read_all_directory, "users_data.txt")
        if (not path.isfile(file_path)):
            raise ValueError("File does not exist")
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            users_data = {user: set(user_data)
                          for user, user_data in data.items()}
            StorageEmulator.storage |= users_data
