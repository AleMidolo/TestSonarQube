class ArgumentParser:
    def __init__(self):
        self.arguments = {}
        self.required = set()
        self.types = {}

    def parse_arguments(self, command_string):
        args = command_string.split()[1:]
        for i in range(len(args)):
            arg = args[i]
            if arg.startswith('--'):
                self._parse_long_argument(arg)
            elif arg.startswith('-'):
                self._parse_short_argument(args, i, arg)

        return self._check_missing_arguments()

    def _parse_long_argument(self, arg):
        key_value = arg[2:].split('=')
        if len(key_value) == 2:
            self.arguments[key_value[0]] = self._convert_type(key_value[0], key_value[1])
        else:
            self.arguments[key_value[0]] = True

    def _parse_short_argument(self, args, i, arg):
        key = arg[1:]
        if i + 1 < len(args) and not args[i + 1].startswith('-'):
            self.arguments[key] = self._convert_type(key, args[i + 1])
        else:
            self.arguments[key] = True

    def _check_missing_arguments(self):
        missing_args = self.required - set(self.arguments.keys())
        if missing_args:
            return False, missing_args
        return True, None

    def get_argument(self, key):
        return self.arguments.get(key)

    def add_argument(self, arg, required=False, arg_type=str):
        if required:
            self.required.add(arg)
        self.types[arg] = arg_type

    def _convert_type(self, arg, value):
        try:
            return self.types[arg](value)
        except (ValueError, KeyError):
            return value