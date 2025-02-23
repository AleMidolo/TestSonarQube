import argparse

def make_parsers():
    """
    Crea un parser di livello superiore e i suoi sottoparser, quindi restituiscili come una tupla.
    """
    main_parser = argparse.ArgumentParser(description="Parser di livello superiore")
    
    subparsers = main_parser.add_subparsers(dest='command', required=True)

    # Sottoparser per il comando 'comando1'
    parser1 = subparsers.add_parser('comando1', help='Descrizione del comando 1')
    parser1.add_argument('--opzione1', type=int, help='Opzione per il comando 1')

    # Sottoparser per il comando 'comando2'
    parser2 = subparsers.add_parser('comando2', help='Descrizione del comando 2')
    parser2.add_argument('--opzione2', type=str, help='Opzione per il comando 2')

    return main_parser, subparsers