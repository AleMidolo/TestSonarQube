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
    
    # Pattern explanation:
    # (?<!Mr) - negative lookbehind to exclude "Mr."
    # [.?] - match . or ?
    # (?=\s|$) - positive lookahead for space or end of string
    # We split on these patterns and then reconstruct sentences
    
    if not sentences_string:
        return []
    
    # Split by . or ? followed by space or end, but not after "Mr"
    pattern = r'(?<!Mr)[.?](?=\s|$)'
    
    # Find all split positions
    parts = re.split(pattern, sentences_string)
    
    # Find all delimiters (. or ?)
    delimiters = re.findall(pattern, sentences_string)
    
    # Reconstruct sentences by combining parts with their delimiters
    sentences = []
    for i, part in enumerate(parts):
        part = part.strip()
        if part:
            # Find the actual delimiter from the original string
            if i < len(parts) - 1:
                # Look for the delimiter after this part in the original string
                start_pos = sentences_string.find(part)
                end_pos = start_pos + len(part)
                # Find the next . or ? after this part
                remaining = sentences_string[end_pos:]
                if remaining and remaining.lstrip() and remaining[0] in '.?':
                    sentences.append(part + remaining[0])
                else:
                    for j, char in enumerate(remaining):
                        if char in '.?':
                            sentences.append(part + char)
                            break
            else:
                # Last part - check if it ends with . or ?
                if sentences_string.rstrip() and sentences_string.rstrip()[-1] in '.?':
                    sentences.append(part + sentences_string.rstrip()[-1])
                else:
                    sentences.append(part)
    
    # Alternative simpler approach using regex
    sentences = []
    pattern = r'(?:(?<!Mr)\.|[?])(?:\s+|$)'
    last_end = 0
    
    for match in re.finditer(pattern, sentences_string):
        sentence = sentences_string[last_end:match.end()].strip()
        if sentence:
            sentences.append(sentence)
        last_end = match.end()
    
    return sentences