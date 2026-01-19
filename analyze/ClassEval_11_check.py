@staticmethod
def check(args):
    """
    Controlla se i parametri sono legali, args deve essere maggiore o uguale a 0 e deve essere pari, altrimenti solleva ValueError.
    :param args: Parametri da controllare, lista.
    :return: Nessuno.
    >>> bit_status_util = BitStatusUtil()
    >>> bit_status_util.check([2,3,4])
    Traceback (most recent call last):
    ...
    ValueError: 3 non è pari
    """
    for arg in args:
        if arg < 0:
            raise ValueError(f"{arg} non è maggiore o uguale a 0")
        if arg % 2 != 0:
            raise ValueError(f"{arg} non è pari")