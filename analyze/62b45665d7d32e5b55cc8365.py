def parse_arguments(*unparsed_arguments):
    import argparse
    
    # Create main parser
    parser = argparse.ArgumentParser(description='Command line argument parser')
    
    # Add global arguments that apply to all subcommands
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose output')
    
    # Create subparsers object to handle subcommands
    subparsers = parser.add_subparsers(dest='command')
    
    # Initialize dictionary to store parsed arguments
    parsed_args = {}
    
    # If no arguments provided, show help and exit
    if not unparsed_arguments:
        parser.print_help()
        return {}
        
    try:
        # Parse the arguments
        args = parser.parse_args(unparsed_arguments[0])
        
        # Store global arguments
        parsed_args['global'] = args
        
        # Store subcommand arguments if a subcommand was used
        if args.command:
            parsed_args[args.command] = args
            
        return parsed_args
        
    except Exception as e:
        parser.print_help()
        return {}