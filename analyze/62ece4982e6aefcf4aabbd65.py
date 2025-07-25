def parser_flags(parser):
    """
    Dado una instancia de 'argparse.ArgumentParser', devuelve sus banderas de argumentos en una cadena separada por espacios.
    """
    flags = []
    # Iterate through all actions (arguments) defined in the parser
    for action in parser._actions:
        # Get all option strings (flags) for this argument
        for opt in action.option_strings:
            # Add the flag to our list if it starts with '-'
            if opt.startswith('-'):
                flags.append(opt)
    
    # Join all flags with spaces and return
    return ' '.join(flags)