def split_sentences(self, text):
    """
    Divide el texto en una lista de oraciones sin puntuación, excepto la última oración
    :param text: Texto a dividir
    :return: Lista de texto dividido
    >>> ru = RegexUtils()
    >>> ru.split_sentences("Aaa. Bbbb? Ccc!")
    ['Aaa', 'Bbbb', 'Ccc!']
    """
    import re
    
    # Split by sentence-ending punctuation (., ?, !)
    sentences = re.split(r'[.?!]\s*', text)
    
    # Remove empty strings from the result
    sentences = [s.strip() for s in sentences if s.strip()]
    
    # If the original text ends with punctuation, we need to add it back to the last sentence
    if sentences and text.strip():
        # Find the last punctuation mark in the original text
        last_char = text.rstrip()[-1]
        if last_char in '.?!':
            sentences[-1] = sentences[-1] + last_char
    
    return sentences