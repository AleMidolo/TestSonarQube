def split_sentences(self, sentences_string):
    """
    Split a string into a list of sentences. Sentences end with . or ? and with a space after that. Please note that Mr. also end with . but are not sentences.
    :param sentences_string: string, string to split
    :return:list, split sentence list
    >>> ss = SplitSentence()
    >>> ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
    ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?']
    """
    import re
    
    # Handle edge cases
    if not sentences_string or not sentences_string.strip():
        return []
    
    # Pattern explanation:
    # (?<!Mr)  - Negative lookbehind: not preceded by "Mr"
    # [.?]     - Match . or ?
    # (?=\s|$) - Positive lookahead: followed by whitespace or end of string
    pattern = r'(?<!Mr)[.?](?=\s|$)'
    
    # Split by the pattern but keep the delimiters
    parts = re.split(pattern, sentences_string)
    
    # Find all sentence-ending punctuation marks
    delimiters = re.findall(pattern, sentences_string)
    
    # Reconstruct sentences by combining parts with their delimiters
    sentences = []
    for i, part in enumerate(parts):
        if part.strip():  # Only process non-empty parts
            if i < len(delimiters):
                # Add the delimiter back to the sentence
                sentence = part.strip() + delimiters[i]
            else:
                # Last part might not have a delimiter
                sentence = part.strip()
            sentences.append(sentence)
    
    return sentences