def parser_flags(parser):
    return ' '.join([f'--{action.dest}' if action.option_strings else f'-{action.dest}' for action in parser._actions if action.option_strings])