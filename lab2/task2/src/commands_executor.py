from storage import StorageEmulator

class CommandExecutor:
    @staticmethod
    def execute_commands(storage: StorageEmulator,commands_args_pairs):
        for comm, args in commands_args_pairs:
            action = getattr(storage,comm)
            action(args)