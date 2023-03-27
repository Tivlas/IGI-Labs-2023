from commands_logics import CommandAction


class CommandExecutor:
    @staticmethod
    def execute_commands(commands_args_pairs):
        for comm, args in commands_args_pairs:
            CommandAction.actions[comm](args)