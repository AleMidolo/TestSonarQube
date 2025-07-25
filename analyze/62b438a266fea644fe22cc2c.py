def make_parsers():
    """
    शीर्ष-स्तरीय पार्सर और इसके उप-पार्सर बनाएं और उन्हें एक ट्यूपल के रूप में लौटाएं।
    """
    import argparse

    # Create main parser
    parser = argparse.ArgumentParser(description='Main command line tool')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Create parser for 'add' command
    add_parser = subparsers.add_parser('add', help='Add something')
    add_parser.add_argument('item', help='Item to add')
    add_parser.add_argument('--priority', type=int, default=1, help='Priority level')

    # Create parser for 'list' command  
    list_parser = subparsers.add_parser('list', help='List items')
    list_parser.add_argument('--sort', choices=['name', 'date', 'priority'], 
                            default='name', help='Sort order')

    # Create parser for 'remove' command
    remove_parser = subparsers.add_parser('remove', help='Remove an item')
    remove_parser.add_argument('item', help='Item to remove')

    return (parser, add_parser, list_parser, remove_parser)