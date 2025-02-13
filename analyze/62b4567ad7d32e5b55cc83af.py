import argparse

def parse_arguments(*arguments):
    parser = argparse.ArgumentParser()
    parser.add_argument('args', nargs=argparse.REMAINDER)
    return parser.parse_args(arguments)