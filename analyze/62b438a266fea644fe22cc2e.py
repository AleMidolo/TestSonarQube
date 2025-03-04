def parse_arguments(*unparsed_arguments):
    import argparse
    
    # Create main parser
    parser = argparse.ArgumentParser(description='Command line argument parser')
    subparsers = parser.add_subparsers(dest='command')
    
    # Add global arguments to main parser
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose output')
    parser.add_argument('--config', '-c', type=str, help='Path to config file')
    
    # Create subparser for 'run' command
    run_parser = subparsers.add_parser('run', help='Run the application')
    run_parser.add_argument('--input', '-i', required=True, help='Input file')
    run_parser.add_argument('--output', '-o', required=True, help='Output file')
    
    # Create subparser for 'test' command  
    test_parser = subparsers.add_parser('test', help='Run tests')
    test_parser.add_argument('--test-dir', '-t', required=True, help='Test directory')
    
    # Parse arguments
    if len(unparsed_arguments) == 0:
        args = parser.parse_args()
    else:
        args = parser.parse_args(unparsed_arguments)
        
    # Create dictionary to store parsed arguments
    parsed_args = {}
    
    if args.command is None:
        # Store global arguments
        parsed_args['global'] = args
    else:
        # Store command-specific arguments
        parsed_args[args.command] = args
        
    return parsed_args