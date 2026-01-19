def split_sentences(self, sentences_string):
    """
    将字符串拆分为句子列表。句子以 . 或 ? 结尾，并且后面有一个空格。请注意，Mr. 也以 . 结尾，但不是句子。
    :param sentences_string: 字符串, 要拆分的字符串
    :return:list, 拆分后的句子列表
    >>> ss = SplitSentence()
    >>> ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
    ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?']
    """
    import re
    
    # 使用正则表达式匹配句子
    # 匹配以 . 或 ? 结尾且后面跟空格的模式，但排除 Mr. 这种情况
    # 负向前瞻确保 . 前面不是 Mr
    # 使用 split 和 findall 的组合来处理
    
    # 方法：使用正则表达式找到所有句子
    # 匹配模式：非贪婪匹配直到遇到 . 或 ? 后跟空格或字符串结尾
    # 但要排除 Mr. 的情况
    
    sentences = []
    # 匹配句子：从开始到 . 或 ? (但不是 Mr.)，后面跟空格或结尾
    pattern = r'(?:(?!Mr\.)[^.?])+[.?]'
    
    matches = re.findall(pattern, sentences_string)
    
    # 清理结果，去除前后空格
    sentences = [match.strip() for match in matches]
    
    return sentences