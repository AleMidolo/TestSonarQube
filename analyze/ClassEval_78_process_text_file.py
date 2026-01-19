def process_text_file(self, sentences_string):
    """
    Given a text, return the number of words in the longest sentence
    :param sentences_string: string, undivided long sentence
    :return:int, the number of words in the longest sentence
    >>> ss.process_text_file("aaa aaaa. bb bbbb bbb? cccc ccccccc cc ccc. dd ddd?")
    4
    """
    import re
    
    # Split the text into sentences using '.', '?', '!' as delimiters
    sentences = re.split(r'[.?!]+', sentences_string)
    
    max_word_count = 0
    
    for sentence in sentences:
        # Strip whitespace and split by spaces to get words
        words = sentence.strip().split()
        # Count non-empty words
        word_count = len([word for word in words if word])
        max_word_count = max(max_word_count, word_count)
    
    return max_word_count