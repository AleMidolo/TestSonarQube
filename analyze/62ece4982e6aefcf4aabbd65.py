def parser_flags(parser):
    """
    Dado una instancia de 'argparse.ArgumentParser', devuelve sus banderas de argumentos en una cadena separada por espacios.
    """
    flags = []
    # Iterate through all actions (arguments) defined in the parser
    for action in parser._actions:
        # Get all option strings (flags) for this argument
        option_strings = action.option_strings
        # Add non-empty option strings to flags list
        flags.extend([flag for flag in option_strings if flag])
    
    # Join all flags with spaces and return
    return ' '.join(flags)