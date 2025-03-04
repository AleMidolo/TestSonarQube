def get_silent_args(self, args):
    """
    Restituisce l'elenco degli argomenti silenziati.

    :param args: Gli argomenti ricevuti.
    :return: list, nomi degli argomenti silenziati.
    """
    silent_args = [arg for arg in args if arg.startswith('_')]
    return silent_args