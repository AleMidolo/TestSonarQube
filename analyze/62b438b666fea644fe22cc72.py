def parser_flags(parser):
    """
    Dato un'istanza di argparse.ArgumentParser, restituisce i flag degli argomenti
    in una stringa separata da spazi.
    """
    return ' '.join(parser._optionals._actions[1:])  # Skip the first action which is the help