import argparse

def parse_arguments(*arguments):
    """
    Given command-line arguments with which this script was invoked, parse the arguments and return
    them as an ArgumentParser instance.
    """
    parser = argparse.ArgumentParser(description="Parse command-line arguments.")
    # Add any necessary arguments here
    # Example: parser.add_argument('--example', type=str, help='An example argument')
    
    # Parse the arguments
    args = parser.parse_args(arguments)
    return args