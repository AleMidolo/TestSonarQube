def _get_alignment_value(self, alignment):
    """
        Restituisce il valore di allineamento corrispondente alla stringa di allineamento fornita.
        :param alignment: str, la stringa di allineamento ('sinistra', 'centro' o 'destra').
        :return: int, il valore di allineamento.
        """
    alignment = alignment.lower()
    if alignment == 'center' or alignment == 'centro':
        return WD_PARAGRAPH_ALIGNMENT.CENTER
    elif alignment == 'right' or alignment == 'destra':
        return WD_PARAGRAPH_ALIGNMENT.RIGHT
    else:
        return WD_PARAGRAPH_ALIGNMENT.LEFT