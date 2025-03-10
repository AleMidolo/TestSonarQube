import argparse

def make_parsers():
    """
    Crea un parser di livello superiore e i suoi sottoparser, quindi restituiscili come una tupla.
    """
    # Creazione del parser principale
    main_parser = argparse.ArgumentParser(description="Parser principale")

    # Creazione dei sottoparser
    subparsers = main_parser.add_subparsers(title="comandi", dest="comando")

    # Creazione del primo sottoparser
    parser_a = subparsers.add_parser('comando_a', help="Descrizione del comando A")
    parser_a.add_argument('arg1', type=str, help="Argomento 1 per comando A")

    # Creazione del secondo sottoparser
    parser_b = subparsers.add_parser('comando_b', help="Descrizione del comando B")
    parser_b.add_argument('arg2', type=int, help="Argomento 2 per comando B")

    return main_parser, subparsers