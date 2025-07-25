import argparse

def make_parsers():
    """
    Crea un parser di livello superiore e i suoi sottoparser e restituiscili come una tupla.
    """
    # Creazione del parser principale
    main_parser = argparse.ArgumentParser(description="Parser principale")

    # Creazione dei sottoparser
    subparsers = main_parser.add_subparsers(title="comandi", dest="comando")

    # Sottoparser 1
    parser_1 = subparsers.add_parser('comando1', help='Descrizione del comando 1')
    parser_1.add_argument('arg1', type=str, help='Descrizione dell\'argomento 1')

    # Sottoparser 2
    parser_2 = subparsers.add_parser('comando2', help='Descrizione del comando 2')
    parser_2.add_argument('arg2', type=int, help='Descrizione dell\'argomento 2')

    return main_parser, subparsers