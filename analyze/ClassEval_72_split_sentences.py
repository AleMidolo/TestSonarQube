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
    
    # If there are sentences and the original text ends with punctuation,
    # we need to add it back to the last sentence
    if sentences and text.strip():
        # Check if the original text ends with punctuation
        last_char_match = re.search(r'[.?!]\s*$', text)
        if last_char_match:
            # Add the punctuation back to the last sentence
            sentences[-1] += last_char_match.group().strip()
    
    return sentences