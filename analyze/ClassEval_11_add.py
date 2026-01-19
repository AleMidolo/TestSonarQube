@staticmethod
def add(states, stat):
    """
        Aggiungi uno stato allo stato attuale e verifica se i parametri sono legali.
        :param states: Stato attuale, int.
        :param stat: Stato da aggiungere, int.
        :return: Lo stato dopo aver aggiunto lo stato, int.
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.add(2,4)
        6

        """
    BitStatusUtil.check([states, stat])
    if not BitStatusUtil.has(states, stat):
        return states | stat
    return states