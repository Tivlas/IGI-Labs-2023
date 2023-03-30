from command_parser import CommandParser
from commands_executor import CommandExecutor
from storage import StorageEmulator
from colorama import Fore, Style
from os import getcwd
from file_service import FileService


FileService.save_and_read_directory = getcwd()


storage = StorageEmulator()

CommandExecutor.execute_commands(storage,
                                 CommandParser.get_commands_and_args('help'))

user_selected = False
while not user_selected:
    try:
        CommandExecutor.execute_commands(storage,
                                         CommandParser.get_commands_and_args('switch '+input("switch to user: ")))
        user_selected = True
    except Exception as e:
        print(str(e))
        storage.clear()
        continue


while True:
    try:
        CommandExecutor.execute_commands(storage,
                                         CommandParser.get_commands_and_args(input(f"{Fore.YELLOW}{storage.get_cur_user_name()}$ {Style.RESET_ALL}")))
    except Exception as e:
        print(str(e))
        continue
