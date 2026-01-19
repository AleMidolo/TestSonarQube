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
    # (?<!Mr)  - Negative lookbehind: not preceded by "Mr"
    # [.?]     - Match . or ?
    # (?=\s|$) - Positive lookahead: followed by whitespace or end of string
    
    # Split on . or ? that are followed by space or end of string, but not preceded by "Mr"
    sentences = re.split(r'(?<!Mr)[.?](?=\s|$)', sentences_string)
    
    # Filter out empty strings and strip whitespace
    result = []
    for i, sentence in enumerate(sentences):
        sentence = sentence.strip()
        if sentence:
            # Add back the punctuation (except for the last one if it was at the end)
            if i < len(sentences) - 1 or sentences_string.rstrip().endswith(('.', '?')):
                # Determine which punctuation was used
                original_pos = sentences_string.find(sentence)
                if original_pos != -1:
                    end_pos = original_pos + len(sentence)
                    if end_pos < len(sentences_string) and sentences_string[end_pos] in '.?':
                        sentence += sentences_string[end_pos]
                    elif sentences_string.rstrip().endswith('.') and i == len(sentences) - 1:
                        sentence += '.'
                    elif sentences_string.rstrip().endswith('?') and i == len(sentences) - 1:
                        sentence += '?'
            result.append(sentence)
    
    return result