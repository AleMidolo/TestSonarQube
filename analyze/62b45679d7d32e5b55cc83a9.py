def parser_flags(parser):
    """
    Dato un'istanza di argparse.ArgumentParser, restituisce le sue opzioni (flag) 
    degli argomenti in una stringa separata da spazi.
    """
    flags = []
    for action in parser._actions:
        # Skip the help action
        if action.dest == 'help':
            continue
        # Get all option strings (flags) for this argument
        for opt in action.option_strings:
            flags.append(opt)
    
    # Return flags joined by spaces
    return ' '.join(sorted(flags))