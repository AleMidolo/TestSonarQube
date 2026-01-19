def _get_alignment_value(self, alignment):
    """
    Restituisce il valore di allineamento corrispondente alla stringa di allineamento fornita.
    :param alignment: str, la stringa di allineamento ('sinistra', 'centro' o 'destra').
    :return: int, il valore di allineamento.
    """
    alignment_map = {
        'sinistra': 0,
        'centro': 1,
        'destra': 2
    }
    return alignment_map.get(alignment.lower(), 0)