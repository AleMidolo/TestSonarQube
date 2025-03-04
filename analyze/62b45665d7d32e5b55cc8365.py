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
    
    # Add subparser for 'run' command
    run_parser = subparsers.add_parser('run', help='Run the application')
    run_parser.add_argument('--input', type=str, required=True, help='Input file path')
    run_parser.add_argument('--output', type=str, required=True, help='Output file path')
    
    # Add subparser for 'init' command  
    init_parser = subparsers.add_parser('init', help='Initialize configuration')
    init_parser.add_argument('--force', action='store_true', help='Force initialization')
    
    # Parse arguments
    args = parser.parse_args(unparsed_arguments if unparsed_arguments else None)
    
    # Create dict to store parsed arguments
    parsed_args = {}
    
    # Store global arguments
    parsed_args['global'] = argparse.Namespace(
        verbose=args.verbose,
        config=args.config
    )
    
    # Store command-specific arguments if a command was specified
    if args.command:
        command_args = vars(args).copy()
        del command_args['verbose']
        del command_args['config']
        parsed_args[args.command] = argparse.Namespace(**command_args)
    
    return parsed_args