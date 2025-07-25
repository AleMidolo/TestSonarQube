def make_parsers():
    """
    एक शीर्ष-स्तरीय (top-level) पार्सर और उसके सबपार्सर बनाएं और उन्हें एक ट्यूपल के रूप में लौटाएं।
    """
    import argparse

    # Create top level parser
    parser = argparse.ArgumentParser(description='Main command line tool')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Create parser for 'add' command
    add_parser = subparsers.add_parser('add', help='Add a new item')
    add_parser.add_argument('name', help='Name of the item')
    add_parser.add_argument('--value', '-v', help='Value of the item')

    # Create parser for 'list' command  
    list_parser = subparsers.add_parser('list', help='List all items')
    list_parser.add_argument('--sort', '-s', choices=['name', 'value'], 
                            help='Sort output by field')

    # Create parser for 'delete' command
    delete_parser = subparsers.add_parser('delete', help='Delete an item')
    delete_parser.add_argument('name', help='Name of item to delete')

    return (parser, add_parser, list_parser, delete_parser)