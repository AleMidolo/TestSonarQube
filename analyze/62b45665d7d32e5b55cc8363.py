import argparse

def make_parsers():
    parser = argparse.ArgumentParser(description='Top-level parser')
    subparsers = parser.add_subparsers(dest='command')

    # Example subparser 1
    subparser1 = subparsers.add_parser('command1', help='Help for command1')
    subparser1.add_argument('--option1', type=str, help='Option for command1')

    # Example subparser 2
    subparser2 = subparsers.add_parser('command2', help='Help for command2')
    subparser2.add_argument('--option2', type=int, help='Option for command2')

    return parser, subparsers