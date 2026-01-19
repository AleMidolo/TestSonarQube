def calculate_word_frequency(self, words_list):
    """
        Calcula la frecuencia de palabras de cada palabra en la lista de listas de palabras, y ordena el diccionario de frecuencia de palabras por valor en orden descendente.
        :param words_list: una lista de listas de palabras
        :return: diccionario de frecuencia de palabras de las 5 principales, un diccionario de frecuencia de palabras, la clave es la palabra, el valor es la frecuencia
        >>> NLPDataProcessor2.calculate_word_frequency([['this', 'is', 'a', 'test'], ['this', 'is', 'another', 'test']])
        {'this': 2, 'is': 2, 'test': 2, 'a': 1, 'another': 1}
        """
    flat_list = [word for sublist in words_list for word in sublist]
    word_count = Counter(flat_list)
    return dict(word_count.most_common(5))