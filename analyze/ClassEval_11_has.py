@staticmethod
def has(states, stat):
    """
    Controlla se lo stato attuale contiene lo stato specificato e verifica se i parametri sono legali.
    :param states: Stato attuale, int.
    :param stat: Stato specificato, int.
    :return: True se lo stato attuale contiene lo stato specificato, altrimenti False, bool.
    >>> bit_status_util = BitStatusUtil()
    >>> bit_status_util.has(6,2)
    True

    """
    return (states & stat) == stat