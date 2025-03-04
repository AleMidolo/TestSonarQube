def make_parsers():
    """
    शीर्ष-स्तरीय पार्सर और इसके उप-पार्सर बनाएं और उन्हें एक ट्यूपल के रूप में लौटाएं।
    """
    import argparse
    
    # Create main parser
    parser = argparse.ArgumentParser(description='Main command line parser')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Create parser for 'add' command
    add_parser = subparsers.add_parser('add', help='Add items')
    add_parser.add_argument('items', nargs='+', help='Items to add')

    # Create parser for 'remove' command  
    remove_parser = subparsers.add_parser('remove', help='Remove items')
    remove_parser.add_argument('items', nargs='+', help='Items to remove')

    # Create parser for 'list' command
    list_parser = subparsers.add_parser('list', help='List all items')

    return (parser, add_parser, remove_parser, list_parser)