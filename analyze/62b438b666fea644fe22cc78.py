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
                name, help_text = arg
                parser.add_argument(name, help=help_text)
            # Handle tuple arguments with name, type and help text
            elif len(arg) == 3:
                name, arg_type, help_text = arg
                parser.add_argument(name, type=arg_type, help=help_text)
                
    # Parse arguments
    args = parser.parse_args()
    
    return args