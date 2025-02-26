def make_parsers():
    """
    Crear un analizador de nivel superior y sus subanalizadores, y devolverlos como una tupla.
    """
    import argparse

    # Analizador de nivel superior
    main_parser = argparse.ArgumentParser(description='Analizador principal')
    
    # Subanalizador 1
    subparser1 = main_parser.add_subparsers(dest='command1')
    parser1 = subparser1.add_parser('comando1', help='Descripción del comando 1')
    
    # Subanalizador 2
    subparser2 = main_parser.add_subparsers(dest='command2')
    parser2 = subparser2.add_parser('comando2', help='Descripción del comando 2')

    return main_parser, parser1, parser2