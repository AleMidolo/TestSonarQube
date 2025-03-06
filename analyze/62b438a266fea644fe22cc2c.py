import argparse

def make_parsers():
    """
    Crea un parser di livello superiore e i suoi sottoparser, quindi restituiscili come una tupla.
    """
    # Creazione del parser principale
    main_parser = argparse.ArgumentParser(description="Parser principale")

    # Creazione dei sottoparser
    subparsers = main_parser.add_subparsers(title="comandi", dest="comando")

    # Aggiunta di un sottoparser per il comando 'comando1'
    parser_comando1 = subparsers.add_parser('comando1', help="Descrizione del comando1")
    parser_comando1.add_argument('arg1', type=str, help="Descrizione di arg1")

    # Aggiunta di un sottoparser per il comando 'comando2'
    parser_comando2 = subparsers.add_parser('comando2', help="Descrizione del comando2")
    parser_comando2.add_argument('arg2', type=int, help="Descrizione di arg2")

    return main_parser, subparsers