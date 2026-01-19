def process_text_file(self, sentences_string):
    """
    दिए गए पाठ के लिए, सबसे लंबे वाक्य में शब्दों की संख्या लौटाएं
    :param sentences_string: स्ट्रिंग, अविभाजित लंबा वाक्य
    :return:int, सबसे लंबे वाक्य में शब्दों की संख्या
    >>> ss.process_text_file("aaa aaaa. bb bbbb bbb? cccc ccccccc cc ccc. dd ddd?")
    4
    """
    import re
    
    # Split the text into sentences using '.', '?', '!' as delimiters
    sentences = re.split(r'[.?!]', sentences_string)
    
    max_word_count = 0
    
    for sentence in sentences:
        # Strip whitespace and split into words
        words = sentence.strip().split()
        # Count words in current sentence
        word_count = len(words)
        # Update max if current sentence has more words
        if word_count > max_word_count:
            max_word_count = word_count
    
    return max_word_count