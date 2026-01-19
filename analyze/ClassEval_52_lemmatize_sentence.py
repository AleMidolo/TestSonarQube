def lemmatize_sentence(self, sentence):
    """
    Rimuove la punteggiatura dalla frase e tokenizza la frase di input, contrassegna il tag della parte del discorso di ogni parola,
    lemmatizza le parole con parametri diversi in base alle loro parti del discorso e le memorizza in una lista.
    :param sentence: una stringa di frase
    :return: una lista di parole che sono state lemmatizzate.
    >>> lemmatization = Lemmatization()
    >>> lemmatization.lemmatize_sentence("I am running in a race.")
    ['I', 'be', 'run', 'in', 'a', 'race']

    """
    import string
    import nltk
    from nltk.corpus import wordnet
    from nltk.stem import WordNetLemmatizer
    
    # Remove punctuation
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    
    # Tokenize
    tokens = nltk.word_tokenize(sentence)
    
    # POS tagging
    pos_tags = nltk.pos_tag(tokens)
    
    # Initialize lemmatizer
    lemmatizer = WordNetLemmatizer()
    
    # Helper function to convert NLTK POS tags to WordNet POS tags
    def get_wordnet_pos(treebank_tag):
        if treebank_tag.startswith('J'):
            return wordnet.ADJ
        elif treebank_tag.startswith('V'):
            return wordnet.VERB
        elif treebank_tag.startswith('N'):
            return wordnet.NOUN
        elif treebank_tag.startswith('R'):
            return wordnet.ADV
        else:
            return wordnet.NOUN  # default to noun
    
    # Lemmatize each word based on its POS tag
    lemmatized_words = []
    for word, pos in pos_tags:
        wordnet_pos = get_wordnet_pos(pos)
        lemmatized_word = lemmatizer.lemmatize(word, pos=wordnet_pos)
        lemmatized_words.append(lemmatized_word)
    
    return lemmatized_words