@staticmethod
def has(states, stat):
    """
    Verifica si el estado actual contiene el estado especificado y comprueba si los parámetros son legales.
    :param states: Estado actual, int.
    :param stat: Estado especificado, int.
    :return: True si el estado actual contiene el estado especificado, de lo contrario False, bool.
    >>> bit_status_util = BitStatusUtil()
    >>> bit_status_util.has(6,2)
    True

    """
    return (states & stat) == stat