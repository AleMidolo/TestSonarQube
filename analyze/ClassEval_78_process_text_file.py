def process_text_file(self, sentences_string):
    """
    Dada un texto, devuelve el número de palabras en la oración más larga
    :param sentences_string: cadena, oración larga no dividida
    :return:int, el número de palabras en la oración más larga
    >>> ss.process_text_file("aaa aaaa. bb bbbb bbb? cccc ccccccc cc ccc. dd ddd?")
    4
    """
    import re
    
    # Split by sentence delimiters (. ? !)
    sentences = re.split(r'[.?!]+', sentences_string)
    
    max_words = 0
    
    for sentence in sentences:
        # Strip whitespace and split by spaces to count words
        words = sentence.strip().split()
        word_count = len(words)
        
        if word_count > max_words:
            max_words = word_count
    
    return max_words