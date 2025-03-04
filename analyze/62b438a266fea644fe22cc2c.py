def make_parsers():
    """
    Build a top-level parser and its subparsers and return them as a tuple.
    """
    import argparse
    
    # Create the top-level parser
    parser = argparse.ArgumentParser(description='Command line tool')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Create subparsers for different commands
    # Add command
    add_parser = subparsers.add_parser('add', help='Add something')
    add_parser.add_argument('item', help='Item to add')
    
    # Remove command  
    remove_parser = subparsers.add_parser('remove', help='Remove something')
    remove_parser.add_argument('item', help='Item to remove')
    
    # List command
    list_parser = subparsers.add_parser('list', help='List items')
    
    return parser, subparsers