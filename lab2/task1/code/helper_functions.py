from colorama import Fore, Style
from constants import INVALID_INPUT_PATTERN


def color_print(obj, color, end_symbol='\n'):
    print(f"{color}{obj}{Style.RESET_ALL}", end=end_symbol)


def print_result(results):
    for k, v in results.items():
        color_print(k, Fore.YELLOW, ' -> ')
        print(v)


def is_input_valid(text):
    is_valid = True if INVALID_INPUT_PATTERN.findall(text) == [] else False
    return is_valid
