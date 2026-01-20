def lemmatize_sentence(self, sentence):
    """
    Elimina la puntuación de la oración y tokeniza la oración de entrada, marca la etiqueta de parte del discurso de cada palabra,
    lematiza las palabras con diferentes parámetros basados en sus partes del discurso y las almacena en una lista.
    :param sentence: una cadena de texto que representa una oración
    :return: una lista de palabras que han sido lematizadas.
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
    
    # Tokenize the sentence
    tokens = nltk.word_tokenize(sentence)
    
    # POS tag the tokens
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
            return wordnet.NOUN  # Default to noun
    
    # Lemmatize each word based on its POS tag
    lemmatized_words = []
    for word, pos in pos_tags:
        wordnet_pos = get_wordnet_pos(pos)
        lemmatized_word = lemmatizer.lemmatize(word, pos=wordnet_pos)
        lemmatized_words.append(lemmatized_word)
    
    return lemmatized_words