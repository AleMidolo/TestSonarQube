import argparse

def parse_arguments(*arguments):
    """
    Given command-line arguments with which this script was invoked, parse the arguments and return
    them as an ArgumentParser instance.
    """
    parser = argparse.ArgumentParser()
    
    for arg in arguments:
        parser.add_argument(arg)
    
    return parser.parse_args(arguments)