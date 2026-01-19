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
                # Find what delimiter comes after this part
                start_pos = sentences_string.find(part)
                if start_pos != -1:
                    end_pos = start_pos + len(part)
                    # Look for . or ? after the part
                    if end_pos < len(sentences_string) and sentences_string[end_pos] in '.?':
                        sentences.append(part + sentences_string[end_pos])
                    else:
                        sentences.append(part)
            else:
                # Last part - check if original string ends with . or ?
                if sentences_string.rstrip() and sentences_string.rstrip()[-1] in '.?':
                    sentences.append(part + sentences_string.rstrip()[-1])
                else:
                    sentences.append(part)
    
    return sentences