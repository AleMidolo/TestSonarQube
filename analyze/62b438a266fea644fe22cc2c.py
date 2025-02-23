def make_parsers():
    """
    Crear un analizador de nivel superior y sus subanalizadores, y devolverlos como una tupla.
    """
    import argparse

    # Analizador de nivel superior
    top_parser = argparse.ArgumentParser(description='Analizador de nivel superior')
    
    # Subanalizador 1
    sub_parser1 = top_parser.add_subparsers(dest='subcommand1')
    parser_a = sub_parser1.add_parser('comando_a', help='Descripción del comando A')
    
    # Subanalizador 2
    sub_parser2 = top_parser.add_subparsers(dest='subcommand2')
    parser_b = sub_parser2.add_parser('comando_b', help='Descripción del comando B')

    return top_parser, parser_a, parser_b