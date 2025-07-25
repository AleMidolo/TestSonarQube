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
    add_parser = subparsers.add_parser('add', help='Add something')
    add_parser.add_argument('item', help='Item to add')
    add_parser.add_argument('--priority', type=int, default=1, help='Priority level')
    
    # Create "remove" subparser  
    remove_parser = subparsers.add_parser('remove', help='Remove something')
    remove_parser.add_argument('item', help='Item to remove')
    
    # Create "list" subparser
    list_parser = subparsers.add_parser('list', help='List items')
    list_parser.add_argument('--sort', choices=['asc', 'desc'], help='Sort order')
    
    # Parse arguments
    args = parser.parse_args(unparsed_arguments)
    
    # Create dictionary to store parsed arguments
    parsed_args = {}
    
    if args.command:
        # Store subparser arguments under command name
        parsed_args[args.command] = args
    else:
        # Store global arguments under "global"
        parsed_args['global'] = args
        
    return parsed_args