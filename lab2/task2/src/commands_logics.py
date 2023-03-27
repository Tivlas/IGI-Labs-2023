from storage import StorageEmulator
from builtins import exit as sys_exit
import re
from constants import HELP_INFO
from file_service import FileService
import json


class CommandAction:

    @staticmethod
    def switch(username):

        username = username[0]
        while StorageEmulator.cur_user != '':
            choice = input(
                f"Wanna save {StorageEmulator.cur_user}'s container (y/n): ")
            if choice == 'y':
                file_path = input("File path: ")
                FileService.save(file_path)
                break
            elif choice == 'n':
                break
            else:
                print("Invalid choice!")

        if (username not in StorageEmulator.storage.keys()):
            StorageEmulator.storage[username] = set()
            StorageEmulator.cur_user = username
        else:
            StorageEmulator.cur_user = username

        while True:
            choice = input(
                f"Wanna load specific container for {username} (y/n): ")
            if choice == 'y':
                file_path = input("File path: ")
                try:
                    FileService.load(file_path)
                except json.decoder.JSONDecodeError:
                    print("Invalid data in provided file")
                    continue
                break
            elif choice == 'n':
                break
            else:
                print("Invalid choice!")

    @staticmethod
    def add(keys):
        if StorageEmulator.cur_user == '':
            raise Exception("User is not selected!")
        for key in keys:
            try:
                StorageEmulator.storage[StorageEmulator.cur_user].add(
                    int(key))
            except:
                StorageEmulator.storage[StorageEmulator.cur_user].add(key)

    @staticmethod
    def remove(key):
        key = key[0]
        if StorageEmulator.cur_user == '':
            raise Exception("User is not selected!")
        try:
            StorageEmulator.storage[StorageEmulator.cur_user].discard(
                int(key))
        except:
            StorageEmulator.storage[StorageEmulator.cur_user].discard(key)

    @staticmethod
    def list(_):
        if StorageEmulator.cur_user == '':
            raise Exception("User is not selected!")
        data = StorageEmulator.storage[StorageEmulator.cur_user]
        print(data)

    @staticmethod
    def exit(_):
        if StorageEmulator.cur_user == '':
            raise Exception("User is not selected!")
        while True:
            choice = input(
                f"Wanna save {StorageEmulator.cur_user}'s container (y/n): ")
            if choice == 'y':
                file_path = input("File path: ")
                FileService.save(file_path)
                break
            elif choice == 'n':
                break
            else:
                print("Invalid choice!")
        FileService.save_all()
        sys_exit()

    @staticmethod
    def find(keys):
        if StorageEmulator.cur_user == '':
            raise Exception("User is not selected!")
        st_keys = set(keys)
        found_keys = StorageEmulator.storage[StorageEmulator.cur_user].intersection(
            st_keys)
        if found_keys:
            print(found_keys)
        else:
            print("No such elements")

    @staticmethod
    def grep(pattern):
        if StorageEmulator.cur_user == '':
            raise Exception("User is not selected!")
        found_at_least_one = False
        pattern = pattern[0]
        stored_items = StorageEmulator.storage[StorageEmulator.cur_user]
        for item in stored_items:
            if re.search(pattern, str(item)):
                print(item)
                found_at_least_one = True
        if not found_at_least_one:
            print("No such elements")

    @staticmethod
    def help(_):
        if StorageEmulator.cur_user == '':
            raise Exception("User is not selected!")
        print(HELP_INFO)

    @staticmethod
    def save(file_path):
        file_path = file_path[0]
        FileService.save(file_path)

    @staticmethod
    def load(file_path):
        file_path = file_path[0]
        try:
            FileService.load(file_path)
        except json.decoder.JSONDecodeError:
            print("Invalid data in provided file")

    actions = {"switch": switch, "add": add, "find": find, "grep": grep,
               "remove": remove, "list": list, "exit": exit, "help": help, "save": save, "load": load}
