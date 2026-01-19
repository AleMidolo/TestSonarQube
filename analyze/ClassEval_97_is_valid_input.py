def is_valid_input(self, textnum):
    """
    检查输入文本是否仅包含可以转换为数字的有效单词。
    :param textnum: 包含表示数字的单词的输入文本。
    :return: 如果输入有效则返回 True，否则返回 False。
    >>> w2n = Words2Numbers()
    >>> w2n.is_valid_input("thirty-two")
    False
    """
    # 定义有效的数字单词集合
    valid_words = {
        'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
        'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
        'seventeen', 'eighteen', 'nineteen', 'twenty', 'thirty', 'forty', 'fifty',
        'sixty', 'seventy', 'eighty', 'ninety', 'hundred', 'thousand', 'million',
        'billion', 'trillion', 'point', 'and'
    }
    
    # 将输入文本转换为小写并分割成单词
    textnum = textnum.strip().lower()
    
    # 如果输入为空，返回 False
    if not textnum:
        return False
    
    # 替换连字符为空格，然后分割
    words = textnum.replace('-', ' ').split()
    
    # 检查每个单词是否在有效单词集合中
    for word in words:
        if word not in valid_words:
            return False
    
    return True