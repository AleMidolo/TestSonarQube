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
    sentences = re.split(r'[.?!]', text)
    
    # Filter out empty strings
    sentences = [s.strip() for s in sentences if s.strip()]
    
    # If there are sentences and the original text ends with punctuation,
    # add that punctuation back to the last sentence
    if sentences and text.strip():
        # Find the last punctuation mark in the original text
        last_char = text.strip()[-1]
        if last_char in '.?!':
            sentences[-1] = sentences[-1] + last_char
    
    return sentences