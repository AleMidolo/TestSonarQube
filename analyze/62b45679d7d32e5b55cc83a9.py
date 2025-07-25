def parser_flags(parser):
    """
    Dada una instancia de 'argparse.ArgumentParser', devuelve sus banderas de argumentos
    en una cadena separada por espacios.
    """
    flags = []
    for action in parser._actions:
        # Obtener todas las opciones (flags) para esta acción
        flags.extend([opt for opt in action.option_strings])
    
    # Unir todas las flags con espacios y devolver
    return ' '.join(sorted(flags))