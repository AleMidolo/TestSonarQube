def make_parsers():
    """Crea un parser di livello superiore e i suoi sottoparser e restituiscili come una tupla."""
    import argparse

    # Parser principale
    parser = argparse.ArgumentParser(description='Gestore di comandi')
    subparsers = parser.add_subparsers(dest='command', help='Comandi disponibili')

    # Sottoparser per il comando 'add'
    add_parser = subparsers.add_parser('add', help='Aggiungi un nuovo elemento')
    add_parser.add_argument('name', help='Nome dell\'elemento')
    add_parser.add_argument('--value', '-v', help='Valore dell\'elemento')

    # Sottoparser per il comando 'remove' 
    remove_parser = subparsers.add_parser('remove', help='Rimuovi un elemento')
    remove_parser.add_argument('name', help='Nome dell\'elemento da rimuovere')

    # Sottoparser per il comando 'list'
    list_parser = subparsers.add_parser('list', help='Mostra tutti gli elementi')
    list_parser.add_argument('--sort', '-s', action='store_true', help='Ordina gli elementi')

    return parser, add_parser, remove_parser, list_parser