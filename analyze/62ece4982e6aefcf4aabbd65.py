def parser_flags(parser):
    """
    Dado una instancia de 'argparse.ArgumentParser', devuelve sus banderas de argumentos en una cadena separada por espacios.
    """
    return ' '.join([action.option_strings[0] for action in parser._actions if action.option_strings])