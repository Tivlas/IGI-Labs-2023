class Validator:
    @staticmethod
    def validate_commands_and_args(com_args_pairs):
        if len(com_args_pairs) == 0:
            raise ValueError("No command entered")
        for comm, args in com_args_pairs:
            match comm:
                case  'help':
                    if args is not None and len(args) != 0:
                        raise ValueError("help command takes 0 parameters")
                    break
                case 'list':
                    if args is not None and len(args) != 0:
                        raise ValueError("list command takes 0 parameters")
                    break
                case 'exit':
                    if args is not None and len(args) != 0:
                        raise ValueError("exit command takes 0 parameters")
                    break
                case 'remove':
                    if args is None or len(args) != 1:
                        raise ValueError("remove command takes 1 parameter")
                    break
                case 'add':
                    if args is None or len(args) < 1:
                        raise ValueError("add command takes at least 1 parameter")
                    break
                case 'find':
                    if args is None or len(args) < 1:
                        raise ValueError("find command takes at least 1 parameter")
                    break
                case 'grep':
                    if args is None or len(args) != 1:
                        raise ValueError("grep command takes 1 parameter")
                    break
                case 'save':
                    if args is not None and len(args) != 0:
                        raise ValueError("save command takes 1 parameter")
                    break
                case 'load':
                    if args is not None and len(args) != 0:
                        raise ValueError("load command takes 1 parameter")
                    break
                case 'switch':
                    if args is None or len(args) != 1:
                        raise ValueError("switch command takes 1 parameter")
                    break
                case _:
                    raise ValueError("No such command!")
