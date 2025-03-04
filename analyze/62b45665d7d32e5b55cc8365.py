def parse_arguments(*unparsed_arguments):
    """
    Given command-line arguments with which this script was invoked, parse the arguments and return
    them as a dict mapping from subparser name (or "global") to an argparse.Namespace instance.
    """
    import argparse

    # Create main parser
    parser = argparse.ArgumentParser(description='Command line argument parser')
    
    # Add global arguments that apply to all subcommands
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose output')
    
    # Create subparsers object to handle subcommands
    subparsers = parser.add_subparsers(dest='command')
    
    # Initialize dict to store parsed arguments
    parsed_args = {}
    
    # Parse the arguments
    if unparsed_arguments:
        args = parser.parse_args(unparsed_arguments)
    else:
        args = parser.parse_args()
        
    # Store global arguments
    parsed_args['global'] = args
    
    # If a subcommand was used, store its arguments separately
    if args.command:
        parsed_args[args.command] = args
        
    return parsed_args