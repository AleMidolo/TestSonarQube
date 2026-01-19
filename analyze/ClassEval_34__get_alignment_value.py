def _get_alignment_value(self, alignment):
    """
    Returns the alignment value corresponding to the given alignment string.
    :param alignment: str, the alignment string ('left', 'center', or 'right').
    :return: int, the alignment value.
    """
    alignment_map = {
        'left': 0,
        'center': 1,
        'right': 2
    }
    return alignment_map.get(alignment.lower(), 0)