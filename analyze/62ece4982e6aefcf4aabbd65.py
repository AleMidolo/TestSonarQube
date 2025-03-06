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
        if action.option_strings:
            flags.extend(action.option_strings)
    return ' '.join(flags)