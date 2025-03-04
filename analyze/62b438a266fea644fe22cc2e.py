def parse_arguments(*unparsed_arguments):
    """
    Given command-line arguments with which this script was invoked, parse the arguments and return
    them as a dict mapping from subparser name (or "global") to an argparse.Namespace instance.
    """
    import argparse

    # Create main parser
    parser = argparse.ArgumentParser(description='Command line argument parser')
    
    # Add global arguments that apply to all subcommands
    parser.add_argument('--verbose', action='store_true', help='Enable verbose output')
    parser.add_argument('--config', type=str, help='Path to config file')
    
    # Create subparsers
    subparsers = parser.add_subparsers(dest='command')
    
    # Add subparser for different commands
    run_parser = subparsers.add_parser('run')
    run_parser.add_argument('--input', type=str, required=True, help='Input file path')
    run_parser.add_argument('--output', type=str, required=True, help='Output file path')
    
    test_parser = subparsers.add_parser('test') 
    test_parser.add_argument('--test-file', type=str, required=True, help='Test file path')
    
    # Parse arguments
    if len(unparsed_arguments) == 0:
        args = parser.parse_args()
    else:
        args = parser.parse_args(unparsed_arguments)
        
    # Create dict to store parsed arguments
    parsed_args = {}
    
    # Store global arguments
    parsed_args['global'] = argparse.Namespace(
        verbose=args.verbose,
        config=args.config
    )
    
    # Store command-specific arguments
    if args.command == 'run':
        parsed_args['run'] = argparse.Namespace(
            input=args.input,
            output=args.output
        )
    elif args.command == 'test':
        parsed_args['test'] = argparse.Namespace(
            test_file=args.test_file
        )
        
    return parsed_args