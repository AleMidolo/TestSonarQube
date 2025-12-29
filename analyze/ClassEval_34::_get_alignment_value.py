def _get_alignment_value(self, alignment):
    """
        Returns the alignment value corresponding to the given alignment string.
        :param alignment: str, the alignment string ('left', 'center', or 'right').
        :return: int, the alignment value.
        """
    alignment_mapping = {'left': WD_PARAGRAPH_ALIGNMENT.LEFT, 'center': WD_PARAGRAPH_ALIGNMENT.CENTER, 'right': WD_PARAGRAPH_ALIGNMENT.RIGHT}
    return alignment_mapping.get(alignment.lower(), WD_PARAGRAPH_ALIGNMENT.LEFT)