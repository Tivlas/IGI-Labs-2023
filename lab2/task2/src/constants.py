import re
from colorama import Fore, Style

green = Fore.GREEN
default = Style.RESET_ALL

SWITCH_INFO = f"{green}switch{default} <username> — switches to user or creates if such user does not exist. Takes 1 parameter."

ADD_INFO = f"{green}add{default} [parameters] — add parameters to current user storage. Takes at least 1 parameter."

REMOVE_INFO = f"{green}remove{default} <parameter> — removes 1 item from current user storage. Takes 1 parameter."

FIND_INFO = f"{green}find{default} [parameters] — prints all found parameters or message if no parameters found. Takes at least 1 parameter."

LIST_INFO = f"{green}list{default} — prints current user storage items. Takes 0 parameters."

GREP_INFO = f"{green}grep{default} <pattern> — search for items in current user storage that match given pattern. Takes 1 parameter."

LOAD_INFO = f"{green}load{default} None | <path> — loads data from default file (selected by the program) or user-provided file. Takes 0 or 1 parameter."

SAVE_INFO = f"{green}save{default} None | <path> — save data to default file (selected by the program) or user-provided file. Takes 0 or 1 parameter."

EXIT_INFO = f"{green}exit{default} — quits the program. Takes 0 parameters."

ADDITIONAL_INFO = f"{green}Note:{default} command name cannot be a parameter to another command!"

HELP_INFO = f"\n{SWITCH_INFO}\n\n{ADD_INFO}\n\n{REMOVE_INFO}\n\n{FIND_INFO}\n\n{LIST_INFO}\n\n{GREP_INFO}\n\n{LOAD_INFO}\n\n{SAVE_INFO}\n\n{EXIT_INFO}\n\n{ADDITIONAL_INFO}"

COMMAND_PATTERN = re.compile(
    r'(?<!\S)\b(?:add|remove|find|grep|save|load|list|switch|help|exit)\b(?=(?:(?:[^"]*"){2})*[^"]*$)(?<!")')

ARGS_PATTERN = re.compile(r'("[^"]+"|\S+)')
