def _get_alignment_value(self, alignment):
    """
        Devuelve el valor de alineación correspondiente a la cadena de alineación dada.
        :param alignment: str, la cadena de alineación ('izquierda', 'centro' o 'derecha').
        :return: int, el valor de alineación.
        """
    alignment_mapping = {'left': WD_PARAGRAPH_ALIGNMENT.LEFT, 'izquierda': WD_PARAGRAPH_ALIGNMENT.LEFT, 'center': WD_PARAGRAPH_ALIGNMENT.CENTER, 'centro': WD_PARAGRAPH_ALIGNMENT.CENTER, 'right': WD_PARAGRAPH_ALIGNMENT.RIGHT, 'derecha': WD_PARAGRAPH_ALIGNMENT.RIGHT}
    return alignment_mapping.get(alignment.lower(), WD_PARAGRAPH_ALIGNMENT.LEFT)