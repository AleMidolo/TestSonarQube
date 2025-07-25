import argparse

def parse_arguments(*unparsed_arguments):
    """
    Given command-line arguments with which this script was invoked, parse the arguments and return
    them as a dict mapping from subparser name (or "global") to an argparse.Namespace instance.
    """
    parser = argparse.ArgumentParser(description="Parse command-line arguments.")
    subparsers = parser.add_subparsers(dest="subparser_name", help="Sub-command help")

    # Example subparser for a command
    subparser_example = subparsers.add_parser('example', help='Example subcommand')
    subparser_example.add_argument('--example_arg', type=str, help='Example argument')

    # Global arguments
    parser.add_argument('--global_arg', type=str, help='Global argument')

    # Parse the arguments
    args = parser.parse_args(unparsed_arguments)

    # Organize parsed arguments into a dictionary
    parsed_args = {}
    if args.subparser_name:
        parsed_args[args.subparser_name] = args
    else:
        parsed_args['global'] = args

    return parsed_args