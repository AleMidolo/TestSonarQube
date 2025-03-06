def make_parsers():
    """
    Crea un parser di livello superiore e i suoi sottoparser, quindi restituiscili come una tupla.
    """
    import argparse

    # Creazione del parser principale
    parser = argparse.ArgumentParser(description="Parser principale")

    # Creazione dei sottoparser
    subparsers = parser.add_subparsers(title="comandi", dest="comando")

    # Esempio di sottoparser 1
    parser_a = subparsers.add_parser('comando_a', help='Descrizione del comando A')
    parser_a.add_argument('arg1', type=int, help='Descrizione di arg1')

    # Esempio di sottoparser 2
    parser_b = subparsers.add_parser('comando_b', help='Descrizione del comando B')
    parser_b.add_argument('arg2', type=str, help='Descrizione di arg2')

    return parser, subparsers