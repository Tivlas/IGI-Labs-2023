from constants import COMMAND_PATTERN, ARGS_PATTERN
from comand_args_validator import Validator
from itertools import zip_longest


class CommandParser:

    @staticmethod
    def get_commands_and_args(input: str):
        if (input.count('"') % 2 != 0):
            raise ValueError("Wrong number of quotes!")

        commands = COMMAND_PATTERN.findall(input)
        all_args = list(filter(lambda arg: arg != '',
                               COMMAND_PATTERN.split(input)))

        separated_args = []
        for specific_comm_args_as_one_string in all_args:
            specific_comm_args = ARGS_PATTERN.findall(
                specific_comm_args_as_one_string)
            separated_args.append(
                [arg if arg[0] != '"' else arg[1:-1] for arg in specific_comm_args])

        commands_and_args = list(zip_longest(commands, separated_args))

        Validator.validate_commands_and_args(commands_and_args)

        return commands_and_args
