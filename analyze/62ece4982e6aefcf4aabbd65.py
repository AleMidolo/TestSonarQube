def parser_flags(parser):
    """
    Dado una instancia de 'argparse.ArgumentParser', devuelve sus banderas de argumentos en una cadena separada por espacios.
    """
    flags = []
    for action in parser._actions:
        if action.option_strings:
            flags.extend(action.option_strings)
    return ' '.join(flags)