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
    
    # Pattern to split on . or ? followed by a space, but not when preceded by "Sr"
    # We use a negative lookbehind to avoid splitting on "Sr."
    pattern = r'(?<!Sr)([.?]) +'
    
    # Split the string using the pattern
    parts = re.split(pattern, sentences_string)
    
    # Reconstruct sentences by combining text with their punctuation
    sentences = []
    i = 0
    while i < len(parts):
        if i + 1 < len(parts) and parts[i + 1] in '.?':
            # Combine the text with its punctuation mark
            sentences.append(parts[i] + parts[i + 1])
            i += 2
        else:
            # Last part without punctuation or standalone text
            if parts[i].strip():
                sentences.append(parts[i])
            i += 1
    
    return sentences