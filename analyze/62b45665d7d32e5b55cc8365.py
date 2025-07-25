def parse_arguments(*unparsed_arguments):
    import argparse
    
    # Create main parser
    parser = argparse.ArgumentParser(description='Command line argument parser')
    subparsers = parser.add_subparsers(dest='command')

    # Global arguments
    parser.add_argument('-v', '--verbose', action='store_true', help='Increase output verbosity')
    parser.add_argument('--config', type=str, help='Path to config file')

    # Create subparsers for different commands
    run_parser = subparsers.add_parser('run', help='Run the application')
    run_parser.add_argument('--input', type=str, required=True, help='Input file path')
    run_parser.add_argument('--output', type=str, help='Output file path')

    test_parser = subparsers.add_parser('test', help='Run tests')
    test_parser.add_argument('--test-dir', type=str, help='Test directory path')
    test_parser.add_argument('--pattern', type=str, help='Test file pattern')

    # Parse arguments
    if len(unparsed_arguments) == 0:
        args = parser.parse_args()
    else:
        args = parser.parse_args(unparsed_arguments)

    # Create result dictionary
    result = {}
    
    # Add global arguments
    result['global'] = argparse.Namespace(
        verbose=args.verbose,
        config=args.config
    )

    # Add command-specific arguments if a command was specified
    if args.command:
        command_args = vars(args).copy()
        del command_args['command']
        del command_args['verbose']
        del command_args['config']
        result[args.command] = argparse.Namespace(**command_args)

    return result