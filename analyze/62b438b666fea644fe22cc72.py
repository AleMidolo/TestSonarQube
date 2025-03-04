def parser_flags(parser):
    """
    Dato un'istanza di argparse.ArgumentParser, restituisce i flag degli argomenti
    in una stringa separata da spazi.
    """
    return ' '.join([action.option_strings[0] for action in parser._actions if action.option_strings])