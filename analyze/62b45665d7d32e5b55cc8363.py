def make_parsers():
    """
    Crea un parser di livello superiore e i suoi sottoparser e restituiscili come una tupla.
    """
    import argparse

    # Creazione del parser principale
    main_parser = argparse.ArgumentParser(description="Parser principale")

    # Creazione dei sottoparser
    subparsers = main_parser.add_subparsers(title="comandi", dest="comando")

    # Esempio di sottoparser 1
    parser_1 = subparsers.add_parser('comando1', help='Descrizione del comando 1')
    parser_1.add_argument('arg1', type=str, help='Argomento 1 per comando1')

    # Esempio di sottoparser 2
    parser_2 = subparsers.add_parser('comando2', help='Descrizione del comando 2')
    parser_2.add_argument('arg2', type=int, help='Argomento 2 per comando2')

    return main_parser, subparsers