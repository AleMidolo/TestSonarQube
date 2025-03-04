def parser_flags(parser):
    """
    Dato un'istanza di argparse.ArgumentParser, restituisce le sue opzioni (flag) 
    degli argomenti in una stringa separata da spazi.
    """
    flags = []
    # Iterate through all actions (arguments) in the parser
    for action in parser._actions:
        # Get all option strings (flags) for this argument
        for opt in action.option_strings:
            # Add the flag if it starts with '-'
            if opt.startswith('-'):
                flags.append(opt)
    
    # Return flags joined by spaces
    return ' '.join(flags)