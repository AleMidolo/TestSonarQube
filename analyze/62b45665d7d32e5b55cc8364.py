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
    
    # Try parsing with each subparser
    for name, subparser in subparsers.items():
        try:
            # Parse known args, allowing unknown ones to pass through
            parsed, unknown = subparser.parse_known_args(remaining_args)
            if parsed:
                parsed_args[name] = parsed
                # Update remaining args to only those that weren't parsed
                remaining_args = unknown
        except:
            # If parsing fails for this subparser, continue to next one
            continue
            
    return parsed_args, remaining_args