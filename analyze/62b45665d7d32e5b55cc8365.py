def parse_arguments(*unparsed_arguments):
    import argparse
    
    # Create main parser
    parser = argparse.ArgumentParser(description='Command line argument parser')
    
    # Add global arguments
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose output')
    
    # Create subparsers
    subparsers = parser.add_subparsers(dest='command')
    
    # Initialize dictionary to store parsed arguments
    parsed_args = {}
    
    # Parse arguments
    if unparsed_arguments:
        args = parser.parse_args(unparsed_arguments)
    else:
        args = parser.parse_args()
        
    # Store global arguments
    parsed_args['global'] = args
    
    # Store subparser arguments if a command was specified
    if args.command:
        parsed_args[args.command] = args
        
    return parsed_args