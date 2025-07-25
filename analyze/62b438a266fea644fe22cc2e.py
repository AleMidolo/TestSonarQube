def parse_arguments(*unparsed_arguments):
    import argparse
    
    # Create main parser
    parser = argparse.ArgumentParser(description='Command line argument parser')
    
    # Create subparsers object
    subparsers = parser.add_subparsers(dest='command')
    
    # Add global arguments to main parser
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose output')
    parser.add_argument('--config', '-c', help='Path to config file')
    
    # Create "run" subparser
    run_parser = subparsers.add_parser('run', help='Run the application')
    run_parser.add_argument('--input', '-i', required=True, help='Input file path')
    run_parser.add_argument('--output', '-o', required=True, help='Output file path')
    
    # Create "test" subparser  
    test_parser = subparsers.add_parser('test', help='Run tests')
    test_parser.add_argument('--test-dir', '-t', required=True, help='Test directory path')
    
    # Parse arguments
    args = parser.parse_args(unparsed_arguments if unparsed_arguments else None)
    
    # Create return dictionary
    parsed_args = {}
    
    # Add global arguments
    parsed_args['global'] = args
    
    # Add subparser arguments if a command was specified
    if hasattr(args, 'command') and args.command:
        parsed_args[args.command] = args
        
    return parsed_args