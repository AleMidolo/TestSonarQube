@staticmethod
def remove(states, stat):
    """
    Rimuove lo stato specificato dallo stato attuale e verifica se i parametri sono legali.
    :param states: Stato attuale, int.
    :param stat: Stato specificato, int.
    :return: Lo stato dopo aver rimosso lo stato specificato, int.
    >>> bit_status_util = BitStatusUtil()
    >>> bit_status_util.remove(6,2)
    4

    """
    return states & ~stat