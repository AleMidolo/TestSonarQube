def parser_flags(parser):
    """
    Dato un'istanza di argparse.ArgumentParser, restituisce le sue opzioni (flag) 
    degli argomenti in una stringa separata da spazi.
    """
    return ' '.join(flag for action in parser._actions for flag in action.option_strings)