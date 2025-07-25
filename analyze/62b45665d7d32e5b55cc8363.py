import argparse

def make_parsers():
    """
    Build a top-level parser and its subparsers and return them as a tuple.
    """
    parser = argparse.ArgumentParser(description="Top-level parser")
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Example subparser for a command 'foo'
    parser_foo = subparsers.add_parser('foo', help='Foo command help')
    parser_foo.add_argument('--option', type=str, help='Option for foo command')

    # Example subparser for a command 'bar'
    parser_bar = subparsers.add_parser('bar', help='Bar command help')
    parser_bar.add_argument('--flag', action='store_true', help='Flag for bar command')

    return parser, subparsers