def process_text_file(self, sentences_string):
    """
    Dato un testo, restituisce il numero di parole nella frase più lunga
    :param sentences_string: stringa, frase lunga non divisa
    :return:int, il numero di parole nella frase più lunga
    >>> ss.process_text_file("aaa aaaa. bb bbbb bbb? cccc ccccccc cc ccc. dd ddd?")
    4
    """
    import re
    
    # Split the text into sentences using . ? ! as delimiters
    sentences = re.split(r'[.?!]+', sentences_string)
    
    max_word_count = 0
    
    for sentence in sentences:
        # Strip whitespace and split by spaces to get words
        words = sentence.strip().split()
        word_count = len(words)
        
        if word_count > max_word_count:
            max_word_count = word_count
    
    return max_word_count