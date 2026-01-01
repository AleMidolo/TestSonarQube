def _get_alignment_value(self, alignment):
    """
        返回与给定对齐字符串对应的对齐值。
        :param alignment: str，对齐字符串（'left', 'center', 或 'right'）。
        :return: int，对齐值。
        """
    alignment_mapping = {'left': WD_PARAGRAPH_ALIGNMENT.LEFT, 'center': WD_PARAGRAPH_ALIGNMENT.CENTER, 'right': WD_PARAGRAPH_ALIGNMENT.RIGHT}
    return alignment_mapping.get(alignment.lower(), WD_PARAGRAPH_ALIGNMENT.LEFT)