def parse_arguments(*unparsed_arguments):
    import argparse
    
    # Create main parser
    parser = argparse.ArgumentParser(description='Command line argument parser')
    
    # Create subparsers object
    subparsers = parser.add_subparsers(dest='command')
    
    # Add global arguments to main parser
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose output')
    parser.add_argument('--config', '-c', help='Path to config file')
    
    # Create "add" subparser
    add_parser = subparsers.add_parser('add', help='Add items')
    add_parser.add_argument('items', nargs='+', help='Items to add')
    
    # Create "remove" subparser  
    remove_parser = subparsers.add_parser('remove', help='Remove items')
    remove_parser.add_argument('items', nargs='+', help='Items to remove')
    
    # Parse arguments
    args = parser.parse_args(unparsed_arguments if unparsed_arguments else None)
    
    # Create dictionary to store parsed arguments
    parsed_args = {}
    
    if args.command:
        # Store subparser arguments
        parsed_args[args.command] = args
    else:
        # Store global arguments
        parsed_args['global'] = args
        
    return parsed_args