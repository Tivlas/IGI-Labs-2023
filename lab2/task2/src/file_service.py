import json
from os import path, getcwd, makedirs


class FileService:
    save_and_read_directory = getcwd()

    @staticmethod
    def save(cur_user_name, cur_user_set):
        file_path = path.join(FileService.save_and_read_directory,
                              'users_data', ''.join(([cur_user_name, '.json'])))
        makedirs(path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as f:
            data = list(cur_user_set)
            json.dump(data, f, ensure_ascii=False, indent=4)

    @staticmethod
    def load(cur_user_name):
        file_path = path.join(FileService.save_and_read_directory,
                              'users_data', ''.join(([cur_user_name, '.json'])))
        if not path.isfile(file_path):
            raise ValueError("Container for this user does not exist")
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return set(data)
