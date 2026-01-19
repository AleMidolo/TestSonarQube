def get_pos_tag(self, sentence):
    """
    Remove punctuations of the sentence and tokenizes the input sentence, mark the part of speech tag of each word.
    :param sentence: a sentence str
    :return: list, part of speech tag of each word in the sentence.
    >>> lemmatization = Lemmatization()
    >>> lemmatization.get_pos_tag("I am running in a race.")
    ['PRP', 'VBP', 'VBG', 'IN', 'DT', 'NN']

    """
    import string
    import nltk
    
    # Remove punctuation from the sentence
    translator = str.maketrans('', '', string.punctuation)
    sentence_no_punct = sentence.translate(translator)
    
    # Tokenize the sentence
    tokens = nltk.word_tokenize(sentence_no_punct)
    
    # Get POS tags
    pos_tags = nltk.pos_tag(tokens)
    
    # Extract only the tags (second element of each tuple)
    tags_only = [tag for word, tag in pos_tags]
    
    return tags_only