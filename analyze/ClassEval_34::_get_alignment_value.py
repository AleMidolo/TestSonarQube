def _get_alignment_value(self, alignment):
    """
        Returns the alignment value corresponding to the given alignment string.
        :param alignment: str, the alignment string ('left', 'center', or 'right').
        :return: int, the alignment value.
        """
    if alignment == 'center':
        return WD_PARAGRAPH_ALIGNMENT.CENTER
    elif alignment == 'right':
        return WD_PARAGRAPH_ALIGNMENT.RIGHT
    else:
        return WD_PARAGRAPH_ALIGNMENT.LEFT