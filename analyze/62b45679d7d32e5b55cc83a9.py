def parser_flags(parser):
    flags = []
    for action in parser._actions:
        # Skip the default help action
        if action.dest == 'help':
            continue
        # Add all option strings (flags) for this argument
        flags.extend(action.option_strings)
    # Return flags joined by spaces
    return ' '.join(sorted(flags))