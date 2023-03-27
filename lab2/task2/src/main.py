from command_parser import CommandParser
from commands_executor import CommandExecutor
from storage import StorageEmulator
from colorama import Fore, Style
from os import getcwd
from file_service import FileService

FileService.save_and_read_all_directory = getcwd()

user_selected = False
while not user_selected:
    try:
        CommandExecutor.execute_commands(
            CommandParser.get_commands_and_args(input("switch to user: ")))
        user_selected = True
    except Exception as e:
        print(e.args[0])
        continue
try:
    while True:
        choice = input(
            f"Wanna load containers from previous run of the program (y/n): ")
        if choice == 'y':
            FileService.load_all()
            print("Containers were loaded, type list to see contents")
            break
        elif choice == 'n':
            break
        else:
            print("Invalid choice!")
except:
    print("Containers not found. Load it from file or fill manually")

while True:
    try:
        CommandExecutor.execute_commands(
            CommandParser.get_commands_and_args(input(f"{Fore.YELLOW}{StorageEmulator.cur_user}$ {Style.RESET_ALL}")))
    except Exception as e:
        print(e.args[0])
        continue
