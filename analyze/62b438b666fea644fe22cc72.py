def parser_flags(parser):
    return " ".join([action.option_strings[0] for action in parser._actions if action.option_strings])