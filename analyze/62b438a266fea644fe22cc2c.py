def make_parsers():
    """
    Build a top-level parser and its subparsers and return them as a tuple.
    """
    import argparse

    # Create the top-level parser
    parser = argparse.ArgumentParser(description="Top-level parser")

    # Create subparsers for the top-level parser
    subparsers = parser.add_subparsers(dest="command", help="Sub-command help")

    # Example: Add a subparser for a 'foo' command
    foo_parser = subparsers.add_parser('foo', help='foo help')
    foo_parser.add_argument('--bar', type=int, help='bar help')

    # Example: Add a subparser for a 'baz' command
    baz_parser = subparsers.add_parser('baz', help='baz help')
    baz_parser.add_argument('--qux', type=str, help='qux help')

    return parser, subparsers