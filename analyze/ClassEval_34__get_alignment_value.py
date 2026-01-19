def _get_alignment_value(self, alignment):
    """
    返回与给定对齐字符串对应的对齐值。
    :param alignment: str，对齐字符串（'left', 'center', 或 'right'）。
    :return: int，对齐值。
    """
    alignment_map = {
        'left': 0,
        'center': 1,
        'right': 2
    }
    return alignment_map.get(alignment.lower(), 0)