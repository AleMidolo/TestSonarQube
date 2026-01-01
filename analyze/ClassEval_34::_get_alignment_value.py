def _get_alignment_value(self, alignment):
    """
        返回与给定对齐字符串对应的对齐值。
        :param alignment: str，对齐字符串（'left', 'center', 或 'right'）。
        :return: int，对齐值。
        """
    if alignment == 'left':
        return WD_PARAGRAPH_ALIGNMENT.LEFT
    elif alignment == 'center':
        return WD_PARAGRAPH_ALIGNMENT.CENTER
    elif alignment == 'right':
        return WD_PARAGRAPH_ALIGNMENT.RIGHT
    else:
        raise ValueError("Invalid alignment value. Use 'left', 'center', or 'right'.")