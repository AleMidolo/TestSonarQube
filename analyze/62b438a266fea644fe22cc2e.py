def parse_arguments(*unparsed_arguments):
    """
    Given command-line arguments with which this script was invoked, parse the arguments and return
    them as a dict mapping from subparser name (or "global") to an argparse.Namespace instance.
    """
    import argparse

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subparser_name')

    # Example subparser for 'command1'
    command1_parser = subparsers.add_parser('command1')
    command1_parser.add_argument('--option1', type=str, help='Option for command1')

    # Example subparser for 'command2'
    command2_parser = subparsers.add_parser('command2')
    command2_parser.add_argument('--option2', type=int, help='Option for command2')

    # Parse the arguments
    args = parser.parse_args(unparsed_arguments)

    # Create a dictionary to hold the results
    result = {}
    
    # Store the parsed arguments in the result dictionary
    if args.subparser_name:
        result[args.subparser_name] = args
    else:
        result['global'] = args

    return result