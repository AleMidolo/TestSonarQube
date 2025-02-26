def make_parsers():
    """
    Crear un analizador de nivel superior y sus subanalizadores, y devolverlos como una tupla.
    """
    import argparse

    # Analizador de nivel superior
    top_parser = argparse.ArgumentParser(description='Analizador de nivel superior')
    
    # Subanalizador 1
    sub_parser1 = top_parser.add_subparsers(dest='command1')
    parser1 = sub_parser1.add_parser('subcommand1', help='Ayuda para subcomando 1')
    
    # Subanalizador 2
    sub_parser2 = top_parser.add_subparsers(dest='command2')
    parser2 = sub_parser2.add_parser('subcommand2', help='Ayuda para subcomando 2')

    return top_parser, parser1, parser2