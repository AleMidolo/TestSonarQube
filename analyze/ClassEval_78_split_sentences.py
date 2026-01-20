def split_sentences(self, sentences_string):
    """
    Divide una cadena en una lista de oraciones. Las oraciones terminan con . o ? y con un espacio después de eso. Tenga en cuenta que Sr. también termina con . pero no son oraciones.
    :param sentences_string: string, cadena a dividir
    :return:list, lista de oraciones divididas
    >>> ss = SplitSentence()
    >>> ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
    ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?']
    """
    import re
    
    # Pattern that matches . or ? followed by a space, but not "Sr."
    # We use negative lookbehind to avoid matching "Sr."
    pattern = r'(?<!Sr)([.?])\s+'
    
    # Split by the pattern but keep the delimiters
    parts = re.split(pattern, sentences_string)
    
    # Reconstruct sentences by combining text with their ending punctuation
    sentences = []
    i = 0
    while i < len(parts):
        if parts[i]:  # Skip empty strings
            if i + 1 < len(parts) and parts[i + 1] in '.?':
                # Combine text with its punctuation
                sentences.append(parts[i] + parts[i + 1])
                i += 2
            else:
                # Last sentence or text without following punctuation
                sentences.append(parts[i])
                i += 1
        else:
            i += 1
    
    return sentences