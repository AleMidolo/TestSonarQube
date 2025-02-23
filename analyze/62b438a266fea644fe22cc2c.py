def make_parsers():
    """
    Crear un analizador de nivel superior y sus subanalizadores, y devolverlos como una tupla.
    """
    import argparse

    # Analizador de nivel superior
    top_parser = argparse.ArgumentParser(description='Analizador de nivel superior')
    
    # Subanalizador 1
    subparser1 = top_parser.add_subparsers(dest='subcommand1')
    parser1 = subparser1.add_parser('sub1', help='Subanalizador 1')
    parser1.add_argument('--option1', type=str, help='Opción para subanalizador 1')

    # Subanalizador 2
    subparser2 = top_parser.add_subparsers(dest='subcommand2')
    parser2 = subparser2.add_parser('sub2', help='Subanalizador 2')
    parser2.add_argument('--option2', type=int, help='Opción para subanalizador 2')

    return top_parser, parser1, parser2