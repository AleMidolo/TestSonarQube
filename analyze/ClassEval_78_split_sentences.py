def split_sentences(self, sentences_string):
    """
    Split a string into a list of sentences. Sentences end with . or ? and with a space after that. Please note that Mr. also end with . but are not sentences.
    :param sentences_string: string, string to split
    :return:list, split sentence list
    >>> ss = SplitSentence()
    >>> ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
    ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?']
    """
    if not sentences_string:
        return []
    
    sentences = []
    current_sentence = []
    words = sentences_string.split()
    
    for i, word in enumerate(words):
        current_sentence.append(word)
        
        # Check if word ends with . or ?
        if word.endswith('.') or word.endswith('?'):
            # Check if it's not "Mr." (or similar titles)
            # Mr. is not a sentence ending if there are more words after it
            if word.endswith('.') and word == "Mr.":
                # Don't end the sentence here
                continue
            else:
                # This is a sentence ending
                sentences.append(' '.join(current_sentence))
                current_sentence = []
    
    # Add any remaining words as a sentence
    if current_sentence:
        sentences.append(' '.join(current_sentence))
    
    return sentences