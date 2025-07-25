def parser_flags(parser):
    """
    Dato un'istanza di `argparse.ArgumentParser`, restituisce i flag degli argomenti in una stringa separata da spazi.  
    Args:
        parser: istanza di `argparse.ArgumentParser`

    Returns:
        flag degli argomenti in una stringa separata da spazi
    """
    flags = []
    for action in parser._actions:
        # Skip the help action
        if action.dest == 'help':
            continue
        # Add all option strings (flags) for this argument
        flags.extend(action.option_strings)
    
    # Join all flags with spaces and return
    return ' '.join(flags)