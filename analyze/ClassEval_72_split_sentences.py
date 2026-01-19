def split_sentences(self, text):
    """
    पाठ को वाक्यों की सूची में विभाजित करें बिना विराम चिह्न के, अंतिम वाक्य को छोड़कर
    :param text: विभाजित करने के लिए पाठ
    :return: विभाजित पाठ सूची
    >>> ru = RegexUtils()
    >>> ru.split_sentences("Aaa. Bbbb? Ccc!")
    ['Aaa', 'Bbbb', 'Ccc!']
    """
    import re
    
    # Split on sentence-ending punctuation (., ?, !)
    sentences = re.split(r'[.?!]', text)
    
    # Filter out empty strings and strip whitespace
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
            sentences[-1] += last_punct
    
    return sentences