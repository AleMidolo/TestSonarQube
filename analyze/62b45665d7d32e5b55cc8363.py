def make_parsers():
    """
    Crea un analizador de nivel superior y sus subanalizadores, y devuélvalos como una tupla.
    """
    import argparse

    # Crear el analizador de nivel superior
    parser = argparse.ArgumentParser(description="Analizador de nivel superior")

    # Crear subanalizadores
    subparsers = parser.add_subparsers(dest="command", help="Subcomandos disponibles")

    # Subanalizador 1
    parser_sub1 = subparsers.add_parser("sub1", help="Subcomando 1")
    parser_sub1.add_argument("arg1", type=str, help="Argumento 1 para subcomando 1")

    # Subanalizador 2
    parser_sub2 = subparsers.add_parser("sub2", help="Subcomando 2")
    parser_sub2.add_argument("arg2", type=int, help="Argumento 2 para subcomando 2")

    return parser, subparsers