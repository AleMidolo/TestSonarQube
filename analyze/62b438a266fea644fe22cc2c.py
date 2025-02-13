import argparse

def make_parsers():
    parser = argparse.ArgumentParser(description='Top-level parser')
    subparsers = parser.add_subparsers(dest='command')

    # Example subparser for a command 'foo'
    parser_foo = subparsers.add_parser('foo', help='Foo command help')
    parser_foo.add_argument('--bar', type=str, help='Bar argument for foo')

    # Example subparser for a command 'baz'
    parser_baz = subparsers.add_parser('baz', help='Baz command help')
    parser_baz.add_argument('--qux', type=int, help='Qux argument for baz')

    return parser, subparsers