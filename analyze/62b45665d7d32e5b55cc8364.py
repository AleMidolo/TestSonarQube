def parse_subparser_arguments(unparsed_arguments, subparsers):
    """
    Given a sequence of arguments and a dict from subparser name to argparse.ArgumentParser
    instance, give each requested action's subparser a shot at parsing all arguments. This allows
    common arguments like "--repository" to be shared across multiple subparsers.

    Return the result as a tuple of (a dict mapping from subparser name to a parsed namespace of
    arguments, a list of remaining arguments not claimed by any subparser).
    """
    import argparse

    parsed_results = {}
    remaining_arguments = unparsed_arguments[:]
    
    for name, parser in subparsers.items():
        try:
            # Attempt to parse the arguments for this subparser
            parsed_args, remaining_arguments = parser.parse_known_args(remaining_arguments)
            parsed_results[name] = parsed_args
        except SystemExit:
            # If parsing fails, we can skip this subparser
            continue

    return parsed_results, remaining_arguments