def get_pos_tag(self, sentence):
    """
    Rimuove la punteggiatura dalla frase e tokenizza la frase di input, contrassegnando il tag della parte del discorso di ogni parola.
    :param sentence: una stringa di frase
    :return: lista, tag della parte del discorso di ogni parola nella frase.
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