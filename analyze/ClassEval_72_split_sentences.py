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
    
    # Split on sentence-ending punctuation (., ?, !)
    sentences = re.split(r'[.?!]+\s*', text)
    
    # Remove empty strings from the result
    sentences = [s.strip() for s in sentences if s.strip()]
    
    # If the original text ends with punctuation, preserve it on the last sentence
    if sentences and text.strip():
        # Find the last punctuation mark(s) in the original text
        match = re.search(r'[.?!]+\s*$', text)
        if match:
            sentences[-1] += match.group().strip()
    
    return sentences