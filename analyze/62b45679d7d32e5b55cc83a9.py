def parser_flags(parser):
    """
    Dato un'istanza di argparse.ArgumentParser, restituisce le sue opzioni (flag) 
    degli argomenti in una stringa separata da spazi.
    """
    return ' '.join(option.dest for option in parser._actions if option.option_strings)