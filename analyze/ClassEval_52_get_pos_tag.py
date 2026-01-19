def get_pos_tag(self, sentence):
    """
    Elimina la puntuación de la oración y tokeniza la oración de entrada, marcando la etiqueta de la parte del discurso de cada palabra.
    :param sentence: una oración str
    :return: lista, etiqueta de la parte del discurso de cada palabra en la oración.
    >>> lemmatization = Lemmatization()
    >>> lemmatization.get_pos_tag("I am running in a race.")
    ['PRP', 'VBP', 'VBG', 'IN', 'DT', 'NN']

    """
    import string
    import nltk
    
    # Eliminar puntuación
    translator = str.maketrans('', '', string.punctuation)
    sentence_no_punct = sentence.translate(translator)
    
    # Tokenizar la oración
    tokens = nltk.word_tokenize(sentence_no_punct)
    
    # Obtener las etiquetas POS
    pos_tags = nltk.pos_tag(tokens)
    
    # Extraer solo las etiquetas (sin las palabras)
    tags_only = [tag for word, tag in pos_tags]
    
    return tags_only