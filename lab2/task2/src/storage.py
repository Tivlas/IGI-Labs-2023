from file_service import FileService
from constants import HELP_INFO
import json
import re


class StorageEmulator:
    def __init__(self) -> None:
        self.__cur_user_name = ''
        self.__storage: dict[str, set] = dict()

    def clear(self):
        self.__storage.clear()
        self.__cur_user_name = ''

    def get_cur_user_name(self):
        return self.__cur_user_name

    def switch(self, username):

        username = username[0]
        while self.__cur_user_name != '':
            choice = input(
                f"Wanna save {self.__cur_user_name}'s container (y/n): ")
            if choice == 'y':
                FileService.save(self.__cur_user_name,
                                 self.__storage[self.__cur_user_name])
                self.__storage[self.__cur_user_name].clear()
                break
            elif choice == 'n':
                self.__storage[self.__cur_user_name].clear()
                break
            else:
                print("Invalid choice!")

        if (username not in self.__storage.keys()):
            self.__storage[username] = set()
            self.__cur_user_name = username
        else:
            self.__cur_user_name = username

        while True:
            choice = input(
                f"Wanna load container for {username} (y/n): ")
            if choice == 'y':
                try:
                    self.__storage[self.__cur_user_name] |= FileService.load(
                        self.__cur_user_name)
                except ValueError as ve:
                    if isinstance(ve, json.decoder.JSONDecodeError):
                        print("Invalid data in provided file")
                    else:
                        print(ve.args[0])
                break
            elif choice == 'n':
                break
            else:
                print("Invalid choice!")

    def add(self, keys):
        if self.__cur_user_name == '':
            raise Exception("User is not selected!")
        for key in keys:
            try:
                self.__storage[self.__cur_user_name].add(
                    int(key))
            except:
                self.__storage[self.__cur_user_name].add(key)

    def remove(self, key):
        key = key[0]
        if self.__cur_user_name == '':
            raise Exception("User is not selected!")
        try:
            self.__storage[self.__cur_user_name].discard(
                int(key))
        except:
            self.__storage[self.__cur_user_name].discard(key)

    def list(self, _):
        if self.__cur_user_name == '':
            raise Exception("User is not selected!")
        data = self.__storage[self.__cur_user_name]
        print(data)

    def exit(self, _):
        if self.__cur_user_name == '':
            raise Exception("User is not selected!")
        while True:
            choice = input(
                f"Wanna save {self.__cur_user_name}'s container (y/n): ")
            if choice == 'y':
                FileService.save(self.__cur_user_name,
                                 self.__storage[self.__cur_user_name])
                break
            elif choice == 'n':
                break
            else:
                print("Invalid choice!")
        exit()

    def find(self, keys):
        if self.__cur_user_name == '':
            raise Exception("User is not selected!")
        st_keys = set(keys)
        found_keys = self.__storage[self.__cur_user_name].intersection(
            st_keys)
        if found_keys:
            print(found_keys)
        else:
            print("No such elements")

    def grep(self, pattern):
        if self.__cur_user_name == '':
            raise Exception("User is not selected!")
        found_at_least_one = False
        pattern = pattern[0]
        stored_items = self.__storage[self.__cur_user_name]
        for item in stored_items:
            if re.search(pattern, str(item)):
                print(item)
                found_at_least_one = True
        if not found_at_least_one:
            print("No such elements")

    def help(self, _):
        print(HELP_INFO)

    def save(self, file_path=None):
        if file_path is not None:
            file_path = file_path[0]
        FileService.save(self.__cur_user_name,
                         self.__storage[self.__cur_user_name], file_path)

    def load(self, file_path=None):
        if file_path is not None:
            file_path = file_path[0]
        try:
            self.__storage[self.__cur_user_name] |= FileService.load(
                self.__cur_user_name, file_path)
        except json.decoder.JSONDecodeError:
            print("Invalid data in provided file")
