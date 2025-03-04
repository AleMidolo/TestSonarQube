def parser_flags(parser):
    flags = []
    for action in parser._actions:
        # Skip help action
        if action.dest == 'help':
            continue
        # Get all option strings (flags) for this action
        flags.extend(action.option_strings)
    # Sort flags and join with spaces
    return ' '.join(sorted(flags))