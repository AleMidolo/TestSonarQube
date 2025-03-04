def get_silent_args(self, args):
    """
    Restituisce l'elenco degli argomenti silenziati.

    :param args: Gli argomenti ricevuti.
    :return: list, nomi degli argomenti silenziati.
    """
    silent_args = []
    
    # Check each argument
    for arg in args:
        # If argument starts with @ it is silenced
        if str(arg).startswith('@'):
            # Remove @ and add to silent list
            silent_args.append(str(arg)[1:])
            
    return silent_args