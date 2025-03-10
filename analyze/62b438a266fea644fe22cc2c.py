def make_parsers():
    """
    Crear un analizador de nivel superior y sus subanalizadores, y devolverlos como una tupla.
    """
    import argparse

    # Crear el analizador de nivel superior
    parser = argparse.ArgumentParser(description="Analizador de nivel superior")

    # Crear subanalizadores
    subparsers = parser.add_subparsers(dest="comando", help="Subcomandos disponibles")

    # Subanalizador para el comando 'comando1'
    parser_comando1 = subparsers.add_parser('comando1', help='Descripción del comando1')
    parser_comando1.add_argument('arg1', type=str, help='Argumento 1 para comando1')

    # Subanalizador para el comando 'comando2'
    parser_comando2 = subparsers.add_parser('comando2', help='Descripción del comando2')
    parser_comando2.add_argument('arg2', type=int, help='Argumento 2 para comando2')

    return parser, subparsers