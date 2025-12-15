def _get_alignment_value(self, alignment):
        """
        Restituisce il valore di allineamento corrispondente alla stringa di allineamento fornita.
        :param alignment: str, la stringa di allineamento ('sinistra', 'centro' o 'destra').
        :return: int, il valore di allineamento.
        """
        if alignment == 'left':
            return WD_PARAGRAPH_ALIGNMENT.LEFT
        elif alignment == 'center':
            return WD_PARAGRAPH_ALIGNMENT.CENTER
        elif alignment == 'right':
            return WD_PARAGRAPH_ALIGNMENT.RIGHT
        else:
            raise ValueError("Invalid alignment value. Use 'left', 'center', or 'right'.")