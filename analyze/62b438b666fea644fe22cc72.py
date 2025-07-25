def parser_flags(parser):
    """
    Dada una instancia de 'argparse.ArgumentParser', devuelve sus banderas de argumentos en una cadena separada por espacios.
    """
    return ' '.join([action.dest for action in parser._actions if action.option_strings])