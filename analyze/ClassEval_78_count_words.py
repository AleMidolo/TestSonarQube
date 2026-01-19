def count_words(self, sentence):
    """
    Cuenta el número de palabras en una oración. Ten en cuenta que las palabras están separadas por espacios y que los signos de puntuación y los números no se cuentan como palabras.
    :param sentence:string, oración a contar, donde las palabras están separadas por espacios
    :return:int, número de palabras en la oración
    >>> ss.count_words("abc def")
    2
    """
    if not sentence:
        return 0
    
    words = sentence.split()
    count = 0
    
    for word in words:
        # Remove punctuation from the word
        cleaned_word = ''.join(char for char in word if char.isalpha())
        # Count only if the cleaned word is not empty (contains letters)
        if cleaned_word:
            count += 1
    
    return count