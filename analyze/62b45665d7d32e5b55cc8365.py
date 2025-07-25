import argparse

def parse_arguments(*unparsed_arguments):
    """
    Given command-line arguments with which this script was invoked, parse the arguments and return
    them as a dict mapping from subparser name (or "global") to an argparse.Namespace instance.
    """
    parser = argparse.ArgumentParser(description="Main parser")
    subparsers = parser.add_subparsers(dest="subparser_name", help="Sub-command help")

    # Example subparser 1
    parser_a = subparsers.add_parser('command_a', help='Command A help')
    parser_a.add_argument('--arg1', type=int, help='Argument 1 for command A')

    # Example subparser 2
    parser_b = subparsers.add_parser('command_b', help='Command B help')
    parser_b.add_argument('--arg2', type=str, help='Argument 2 for command B')

    # Global arguments
    parser.add_argument('--global_arg', type=str, help='Global argument')

    # Parse the arguments
    args = parser.parse_args(unparsed_arguments)

    # Organize parsed arguments into a dictionary
    parsed_args = {}
    if args.subparser_name:
        parsed_args[args.subparser_name] = args
    else:
        parsed_args["global"] = args

    return parsed_args