def parser_flags(parser):
    """
    Given an argparse.ArgumentParser instance, return its argument flags in a space-separated
    string.
    """
    return ' '.join([f'--{action.dest}' if action.option_strings == [] else ' '.join(action.option_strings) for action in parser._actions if action.option_strings])