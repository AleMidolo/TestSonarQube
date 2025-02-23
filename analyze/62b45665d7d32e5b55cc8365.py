def parse_arguments(*unparsed_arguments):
    """
    Given command-line arguments with which this script was invoked, parse the arguments and return
    them as a dict mapping from subparser name (or "global") to an argparse.Namespace instance.
    """
    import argparse

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subparser_name')

    # Example subparser for 'foo'
    foo_parser = subparsers.add_parser('foo')
    foo_parser.add_argument('--bar', type=int, help='An integer for bar')

    # Example subparser for 'baz'
    baz_parser = subparsers.add_parser('baz')
    baz_parser.add_argument('--qux', type=str, help='A string for qux')

    # Parse the arguments
    args = parser.parse_args(unparsed_arguments)

    # Create a dictionary to hold the results
    result = {}
    
    # If no subparser was used, return global arguments
    if args.subparser_name is None:
        result['global'] = args
    else:
        result[args.subparser_name] = args

    return result