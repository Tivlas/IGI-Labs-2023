from constants import AVAILABLE_COMMANDS


class Validator:
    @staticmethod
    def validate_commands_and_args(com_args_pairs):
        if len(com_args_pairs) == 0:
            raise ValueError("No command entered")
        for comm, args in com_args_pairs:
            if comm == 'help':
                if args is not None and len(args) != 0:
                    raise ValueError("help command takes 0 parameters")
            elif comm == 'list':
                if args is not None and len(args) != 0:
                    raise ValueError("list command takes 0 parameters")
            elif comm == 'exit':
                if args is not None and len(args) != 0:
                    raise ValueError("exit command takes 0 parameters")
            elif comm == 'remove':
                if len(args) != 1:
                    raise ValueError("remove command takes 1 parameter")
            elif comm == 'add':
                if len(args) < 1:
                    raise ValueError("add command takes at least 1 parameter")
            elif comm == 'find':
                if len(args) < 1:
                    raise ValueError("find command takes at least 1 parameter")
            elif comm == 'grep':
                if len(args) != 1:
                    raise ValueError("grep command takes 1 parameter")
            elif comm == 'save':
                if len(args) != 1:
                    raise ValueError("save command takes 1 parameter")
            elif comm == 'load':
                if len(args) != 1:
                    raise ValueError("load command takes 1 parameter")
            elif comm == 'switch':
                if len(args) != 1:
                    raise ValueError("switch command takes 1 parameter")
            elif comm not in AVAILABLE_COMMANDS:
                raise ValueError("No such command!")
