def construct_stop_word_list(self):
    """
    构建一个包含 'a', 'an', 'the' 的停用词列表。
    :return: 一个停用词列表
    >>> NLPDataProcessor.construct_stop_word_list()
    ['a', 'an', 'the']
    """
    return ['a', 'an', 'the']