def parse_subparser_arguments(unparsed_arguments, subparsers):
    """
    Given a sequence of arguments and a dict from subparser name to argparse.ArgumentParser
    instance, give each requested action's subparser a shot at parsing all arguments. This allows
    common arguments like "--repository" to be shared across multiple subparsers.

    Return the result as a tuple of (a dict mapping from subparser name to a parsed namespace of
    arguments, a list of remaining arguments not claimed by any subparser).
    """
    parsed_args = {}
    remaining_args = list(unparsed_arguments)
    
    for subparser_name, subparser in subparsers.items():
        try:
            # Try to parse the arguments with the current subparser
            parsed, remaining = subparser.parse_known_args(remaining_args)
            if parsed:
                parsed_args[subparser_name] = parsed
                remaining_args = remaining
        except SystemExit:
            # Ignore SystemExit exceptions that argparse might raise
            continue
    
    return parsed_args, remaining_args