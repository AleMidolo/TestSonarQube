@staticmethod
def remove(states, stat):
    """
        Elimina el estado especificado del estado actual y verifica si los parámetros son legales.
        :param states: Estado actual, int.
        :param stat: Estado especificado, int.
        :return: El estado después de eliminar el estado especificado, int.
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.remove(6,2)
        4

        """
    BitStatusUtil.check([states, stat])
    return states & ~stat