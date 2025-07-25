def get_silent_args(self, args):
    """
    Restituisce l'elenco degli argomenti silenziati.

    :param args: Gli argomenti ricevuti.
    :return: list, nomi degli argomenti silenziati.
    """
    silent_args = []
    for arg in args:
        if arg.startswith('--silent-'):
            silent_args.append(arg[len('--silent-'):])
    return silent_args