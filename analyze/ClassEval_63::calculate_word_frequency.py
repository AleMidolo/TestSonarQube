def calculate_word_frequency(self, words_list):
    """
        Calcula la frecuencia de palabras de cada palabra en la lista de listas de palabras, y ordena el diccionario de frecuencia de palabras por valor en orden descendente.
        :param words_list: una lista de listas de palabras
        :return: diccionario de frecuencia de palabras de las 5 principales, un diccionario de frecuencia de palabras, la clave es la palabra, el valor es la frecuencia
        >>> NLPDataProcessor.calculate_word_frequency([['this', 'is', 'a', 'test'], ['this', 'is', 'another', 'test']])
        {'this': 2, 'is': 2, 'test': 2, 'a': 1, 'another': 1}
        """
    word_counter = Counter()
    for words in words_list:
        word_counter.update(words)
    sorted_items = sorted(word_counter.items(), key=lambda x: x[1], reverse=True)
    top_5 = dict(sorted_items[:5])
    return top_5