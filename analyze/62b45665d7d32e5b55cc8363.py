def make_parsers():
    """Crea un parser di livello superiore e i suoi sottoparser e restituiscili come una tupla."""
    import argparse

    # Parser principale
    parser = argparse.ArgumentParser(description='Tool di gestione file')
    subparsers = parser.add_subparsers(dest='command', help='Comandi disponibili')

    # Sottoparser per il comando 'list'
    list_parser = subparsers.add_parser('list', help='Elenca i file in una directory')
    list_parser.add_argument('directory', nargs='?', default='.', help='Directory da elencare')
    list_parser.add_argument('-r', '--recursive', action='store_true', help='Elenca ricorsivamente')

    # Sottoparser per il comando 'copy'
    copy_parser = subparsers.add_parser('copy', help='Copia file')
    copy_parser.add_argument('source', help='File sorgente')
    copy_parser.add_argument('destination', help='Destinazione')
    copy_parser.add_argument('-f', '--force', action='store_true', help='Sovrascrive file esistenti')

    # Sottoparser per il comando 'move'
    move_parser = subparsers.add_parser('move', help='Sposta file')
    move_parser.add_argument('source', help='File sorgente')
    move_parser.add_argument('destination', help='Destinazione')
    move_parser.add_argument('-f', '--force', action='store_true', help='Sovrascrive file esistenti')

    # Sottoparser per il comando 'delete'
    delete_parser = subparsers.add_parser('delete', help='Elimina file')
    delete_parser.add_argument('files', nargs='+', help='File da eliminare')
    delete_parser.add_argument('-r', '--recursive', action='store_true', help='Elimina ricorsivamente')

    return parser, list_parser, copy_parser, move_parser, delete_parser