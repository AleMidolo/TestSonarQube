def is_valid_input(self, textnum):
    """
    检查输入文本是否仅包含可以转换为数字的有效单词。
    :param textnum: 包含表示数字的单词的输入文本。
    :return: 如果输入有效则返回 True，否则返回 False。
    >>> w2n = Words2Numbers()
    >>> w2n.is_valid_input("thirty-two")
    False
    """
    # Define valid number words
    valid_words = {
        'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
        'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
        'seventeen', 'eighteen', 'nineteen', 'twenty', 'thirty', 'forty', 'fifty',
        'sixty', 'seventy', 'eighty', 'ninety', 'hundred', 'thousand', 'million',
        'billion', 'trillion', 'and', 'point'
    }
    
    # Convert to lowercase and split by spaces
    textnum = textnum.lower().strip()
    
    # Split by spaces to get individual words
    words = textnum.split()
    
    # Check each word
    for word in words:
        # Remove hyphens and check each part
        parts = word.split('-')
        for part in parts:
            if part and part not in valid_words:
                return False
    
    return True