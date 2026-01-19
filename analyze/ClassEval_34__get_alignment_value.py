def _get_alignment_value(self, alignment):
    """
        Devuelve el valor de alineación correspondiente a la cadena de alineación dada.
        :param alignment: str, la cadena de alineación ('izquierda', 'centro' o 'derecha').
        :return: int, el valor de alineación.
        """
    alignment = alignment.lower()
    if alignment == 'center' or alignment == 'centro':
        return WD_PARAGRAPH_ALIGNMENT.CENTER
    elif alignment == 'right' or alignment == 'derecha':
        return WD_PARAGRAPH_ALIGNMENT.RIGHT
    else:
        return WD_PARAGRAPH_ALIGNMENT.LEFT