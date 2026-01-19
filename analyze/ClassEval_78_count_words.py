def count_words(self, sentence):
    """
    Count the number of words in a sentence. Note that words are separated by spaces and that punctuation marks and numbers are not counted as words.
    :param sentence:string, sentence to be counted, where words are separated by spaces
    :return:int, number of words in the sentence
    >>> ss.count_words("abc def")
    2
    """
    if not sentence:
        return 0
    
    words = sentence.split()
    count = 0
    
    for word in words:
        # Check if the word contains at least one alphabetic character
        if any(char.isalpha() for char in word):
            count += 1
    
    return count