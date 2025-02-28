import argparse

def parse_arguments(*unparsed_arguments):
    """
    Given command-line arguments with which this script was invoked, parse the arguments and return
    them as a dict mapping from subparser name (or "global") to an argparse.Namespace instance.
    """
    parser = argparse.ArgumentParser(description="Main parser")
    subparsers = parser.add_subparsers(dest="subparser_name", help="Sub-command help")

    # Example subparser for 'command1'
    parser_command1 = subparsers.add_parser('command1', help='Command1 help')
    parser_command1.add_argument('--arg1', type=str, help='Argument 1 for command1')

    # Example subparser for 'command2'
    parser_command2 = subparsers.add_parser('command2', help='Command2 help')
    parser_command2.add_argument('--arg2', type=int, help='Argument 2 for command2')

    # Parse the arguments
    parsed_args = parser.parse_args(unparsed_arguments)

    # Organize the parsed arguments into a dictionary
    result = {}
    if hasattr(parsed_args, 'subparser_name'):
        result[parsed_args.subparser_name] = parsed_args
    else:
        result['global'] = parsed_args

    return result