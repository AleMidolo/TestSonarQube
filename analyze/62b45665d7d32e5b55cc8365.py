import argparse
import sys

def parse_arguments(*unparsed_arguments):
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subparser_name')

    # Example subparser
    subparser_a = subparsers.add_parser('sub_a')
    subparser_a.add_argument('--option_a', type=str, help='Option for subparser A')

    subparser_b = subparsers.add_parser('sub_b')
    subparser_b.add_argument('--option_b', type=int, help='Option for subparser B')

    # Parse the arguments
    args = parser.parse_args(unparsed_arguments)

    # Create a dictionary to hold the results
    result = {}

    # Check if a subparser was used
    if args.subparser_name:
        result[args.subparser_name] = args
    else:
        result['global'] = args

    return result