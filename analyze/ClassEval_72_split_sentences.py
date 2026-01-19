def split_sentences(self, text):
    """
    Split the text into a list of sentences without Punctuation except the last sentence
    :param text: Text to be split
    :return: Split Text List
    >>> ru = RegexUtils()
    >>> ru.split_sentences("Aaa. Bbbb? Ccc!")
    ['Aaa', 'Bbbb', 'Ccc!']
    """
    import re
    
    # Split by sentence-ending punctuation (., ?, !)
    sentences = re.split(r'[.?!]', text)
    
    # Filter out empty strings
    sentences = [s.strip() for s in sentences if s.strip()]
    
    # If there are sentences, we need to add back the punctuation to the last one
    if sentences:
        # Find the last punctuation mark in the original text
        last_punct = ''
        for char in reversed(text):
            if char in '.?!':
                last_punct = char
                break
        
        # Add the punctuation back to the last sentence
        if last_punct:
            sentences[-1] = sentences[-1] + last_punct
    
    return sentences