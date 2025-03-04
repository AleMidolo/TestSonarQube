def parse_arguments(*arguments):
    """
    Given command-line arguments with which this script was invoked, parse the arguments and return
    them as an ArgumentParser instance.
    """
    import argparse
    
    parser = argparse.ArgumentParser(description='Parse command line arguments')
    
    # Add arguments
    parser.add_argument('--input', '-i', type=str, help='Input file path')
    parser.add_argument('--output', '-o', type=str, help='Output file path')
    parser.add_argument('--verbose', '-v', action='store_true', help='Increase output verbosity')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    
    # Parse arguments
    if len(arguments) > 0:
        args = parser.parse_args(arguments)
    else:
        args = parser.parse_args()
        
    return args