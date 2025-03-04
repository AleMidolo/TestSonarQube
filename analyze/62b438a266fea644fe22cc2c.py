def make_parsers():
    """
    Build a top-level parser and its subparsers and return them as a tuple.
    """
    import argparse
    
    # Create top-level parser
    parser = argparse.ArgumentParser(description='Command line tool')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Create subparsers
    run_parser = subparsers.add_parser('run', help='Run the program')
    config_parser = subparsers.add_parser('config', help='Configure settings')
    test_parser = subparsers.add_parser('test', help='Run tests')
    
    # Add arguments to run parser
    run_parser.add_argument('-i', '--input', help='Input file')
    run_parser.add_argument('-o', '--output', help='Output file')
    run_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    
    # Add arguments to config parser
    config_parser.add_argument('--set', help='Set a configuration value')
    config_parser.add_argument('--get', help='Get a configuration value')
    
    # Add arguments to test parser
    test_parser.add_argument('-u', '--unit', action='store_true', help='Run unit tests')
    test_parser.add_argument('-i', '--integration', action='store_true', help='Run integration tests')
    
    return parser, subparsers