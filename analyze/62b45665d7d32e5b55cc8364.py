def parse_subparser_arguments(unparsed_arguments, subparsers):
    import argparse

    parsed_results = {}
    remaining_arguments = unparsed_arguments[:]
    
    for subparser_name, parser in subparsers.items():
        try:
            # Attempt to parse the arguments for the current subparser
            parsed_args, remaining_arguments = parser.parse_known_args(remaining_arguments)
            parsed_results[subparser_name] = parsed_args
        except SystemExit:
            # If parsing fails, we can skip this subparser
            continue

    return parsed_results, remaining_arguments