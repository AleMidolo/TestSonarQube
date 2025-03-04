def parser_flags(parser):
    flags = []
    for action in parser._actions:
        # Skip the help action which is added by default
        if action.dest == 'help':
            continue
        # Add all option strings (flags) for this argument
        flags.extend(action.option_strings)
    # Return flags joined by spaces
    return ' '.join(sorted(flags))