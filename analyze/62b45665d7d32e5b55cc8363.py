import argparse

def make_parsers():
    """
    Build a top-level parser and its subparsers and return them as a tuple.
    """
    # Create the top-level parser
    parser = argparse.ArgumentParser(description="Top-level parser")
    
    # Create subparsers for the top-level parser
    subparsers = parser.add_subparsers(dest="command", help="Sub-command help")
    
    # Example subparser 1
    parser_a = subparsers.add_parser('command_a', help='Command A help')
    parser_a.add_argument('--arg1', type=int, help='Argument 1 for command A')
    
    # Example subparser 2
    parser_b = subparsers.add_parser('command_b', help='Command B help')
    parser_b.add_argument('--arg2', type=str, help='Argument 2 for command B')
    
    return parser, subparsers