import argparse

def make_parsers():
    """Crea un parser di livello superiore e i suoi sottoparser e restituiscili come una tupla."""
    main_parser = argparse.ArgumentParser(description="Parser di livello superiore")
    
    subparsers = main_parser.add_subparsers(dest='command', required=True)

    # Esempio di sottoparser 1
    parser_a = subparsers.add_parser('comando_a', help='Esegui il comando A')
    parser_a.add_argument('--opzione_a', type=int, help='Opzione per il comando A')

    # Esempio di sottoparser 2
    parser_b = subparsers.add_parser('comando_b', help='Esegui il comando B')
    parser_b.add_argument('--opzione_b', type=str, help='Opzione per il comando B')

    return main_parser, subparsers