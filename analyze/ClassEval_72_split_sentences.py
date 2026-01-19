def split_sentences(self, text):
    """
    Suddivide il testo in un elenco di frasi senza punteggiatura tranne l'ultima frase
    :param text: Testo da suddividere
    :return: Elenco di testo suddiviso
    >>> ru = RegexUtils()
    >>> ru.split_sentences("Aaa. Bbbb? Ccc!")
    ['Aaa', 'Bbbb', 'Ccc!']
    """
    import re
    
    if not text:
        return []
    
    # Split by sentence-ending punctuation (., ?, !)
    sentences = re.split(r'[.?!]+\s*', text)
    
    # Remove empty strings
    sentences = [s.strip() for s in sentences if s.strip()]
    
    # If the original text ends with punctuation, we need to add it back to the last sentence
    if sentences and text.strip():
        # Find the last punctuation mark in the original text
        last_punct_match = re.search(r'[.?!]+\s*$', text)
        if last_punct_match:
            # Add the punctuation back to the last sentence
            sentences[-1] = sentences[-1] + last_punct_match.group().strip()
    
    return sentences