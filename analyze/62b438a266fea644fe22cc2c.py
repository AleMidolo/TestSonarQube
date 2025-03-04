def make_parsers():
    """
    Crea un parser di livello superiore e i suoi sottoparser, quindi restituiscili come una tupla.
    """
    import argparse

    # Create main parser
    parser = argparse.ArgumentParser(description='Command line tool')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Create "add" subparser
    add_parser = subparsers.add_parser('add', help='Add a new item')
    add_parser.add_argument('name', help='Name of the item')
    add_parser.add_argument('--quantity', type=int, default=1, help='Quantity to add')

    # Create "list" subparser 
    list_parser = subparsers.add_parser('list', help='List all items')
    list_parser.add_argument('--sort', choices=['name', 'date'], default='name', 
                            help='Sort items by name or date')

    # Create "remove" subparser
    remove_parser = subparsers.add_parser('remove', help='Remove an item')
    remove_parser.add_argument('name', help='Name of item to remove')

    return (parser, add_parser, list_parser, remove_parser)