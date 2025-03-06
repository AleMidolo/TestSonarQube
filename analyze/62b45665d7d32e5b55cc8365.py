import argparse

def parse_arguments(*unparsed_arguments):
    """
    Given command-line arguments with which this script was invoked, parse the arguments and return
    them as a dict mapping from subparser name (or "global") to an argparse.Namespace instance.
    """
    parser = argparse.ArgumentParser(description="Main parser")
    subparsers = parser.add_subparsers(dest="subparser_name", help="Sub-command help")

    # Example subparser
    subparser_example = subparsers.add_parser("example", help="Example subparser")
    subparser_example.add_argument("--example_arg", type=str, help="Example argument")

    # Global arguments
    parser.add_argument("--global_arg", type=str, help="Global argument")

    # Parse the arguments
    parsed_args = parser.parse_args(unparsed_arguments)

    # Organize the parsed arguments into a dictionary
    args_dict = {}
    if hasattr(parsed_args, "subparser_name"):
        args_dict[parsed_args.subparser_name] = parsed_args
    else:
        args_dict["global"] = parsed_args

    return args_dict