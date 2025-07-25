def parser_flags(parser):
    """
    Dato un'istanza di argparse.ArgumentParser, restituisce le sue opzioni (flag) 
    degli argomenti in una stringa separata da spazi.
    """
    flags = []
    # Iterate through all actions (arguments) in the parser
    for action in parser._actions:
        # Get all option strings (flags) for this argument
        option_strings = action.option_strings
        # Add non-empty option strings to flags list
        flags.extend([opt for opt in option_strings if opt])
    
    # Join all flags with spaces and return
    return ' '.join(flags)