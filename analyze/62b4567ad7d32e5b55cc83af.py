def parse_arguments(*arguments):
    import argparse
    
    # Create ArgumentParser instance
    parser = argparse.ArgumentParser(description='Command line argument parser')
    
    # Add arguments to parser
    for arg in arguments:
        if isinstance(arg, str):
            parser.add_argument(arg)
        elif isinstance(arg, tuple):
            # Handle tuple arguments with name and help text
            if len(arg) == 2:
                parser.add_argument(arg[0], help=arg[1])
            # Handle tuple arguments with name, type and help text
            elif len(arg) == 3:
                parser.add_argument(arg[0], type=arg[1], help=arg[2])
                
    # Parse arguments and return
    return parser.parse_args()