from constants import COMMAND_PATTERN, ARGS_PATTERN
from comand_args_validator import Validator
from itertools import zip_longest

class CommandParser:

    @staticmethod
    def get_commands_and_args(input: str):
        if (input.count('"') % 2 != 0):
            raise ValueError("Wrong number of quotes!")

        commands = COMMAND_PATTERN.findall(input)
        args = list(filter(lambda arg: arg != '',
                    COMMAND_PATTERN.split(input)))

        separated_args = []
        for arg in args:
            separated_args.append(ARGS_PATTERN.findall(arg))

        commands_and_args = list(zip_longest(commands, separated_args))

        Validator.validate_commands_and_args(commands_and_args)

        return commands_and_args
