def get_silent_args(self, args):
    """
    Restituisce l'elenco degli argomenti silenziati.

    :param args: Gli argomenti ricevuti.
    :return: list, nomi degli argomenti silenziati.
    """
    silent_args = []
    
    # Iterate through args and check for silent flag
    for arg in args:
        if isinstance(arg, str) and arg.startswith('-s'):
            # Remove -s prefix to get actual argument name
            silent_arg = arg[2:]
            silent_args.append(silent_arg)
            
    return silent_args