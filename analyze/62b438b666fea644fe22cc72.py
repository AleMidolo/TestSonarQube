def parser_flags(parser):
    flags = []
    for action in parser._actions:
        # Skip the default help action
        if action.dest == 'help':
            continue
        # Add all option strings (flags) for this argument
        flags.extend(action.option_strings)
    # Join all flags with spaces and return
    return ' '.join(sorted(flags))