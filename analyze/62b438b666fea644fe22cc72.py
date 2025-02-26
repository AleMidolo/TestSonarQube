def parser_flags(parser):
    """
    Given an argparse.ArgumentParser instance, return its argument flags in a space-separated
    string.
    """
    return ' '.join([action.option_strings[0] for action in parser._actions if action.option_strings])