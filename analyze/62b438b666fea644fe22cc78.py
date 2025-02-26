import argparse

def parse_arguments(*arguments):
    """
    Given command-line arguments with which this script was invoked, parse the arguments and return
    them as an ArgumentParser instance.
    """
    parser = argparse.ArgumentParser()
    
    # Example of adding arguments, modify as needed
    parser.add_argument('--option1', type=str, help='Description for option1')
    parser.add_argument('--option2', type=int, help='Description for option2')
    
    # Parse the provided arguments
    parsed_args = parser.parse_args(arguments)
    
    return parsed_args