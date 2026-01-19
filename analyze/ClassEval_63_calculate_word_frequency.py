def calculate_word_frequency(self, words_list):
    """
    Calcula la frecuencia de palabras de cada palabra en la lista de listas de palabras, y ordena el diccionario de frecuencia de palabras por valor en orden descendente.
    :param words_list: una lista de listas de palabras
    :return: diccionario de frecuencia de palabras de las 5 principales, un diccionario de frecuencia de palabras, la clave es la palabra, el valor es la frecuencia
    >>> NLPDataProcessor.calculate_word_frequency([['this', 'is', 'a', 'test'], ['this', 'is', 'another', 'test']])
    {'this': 2, 'is': 2, 'test': 2, 'a': 1, 'another': 1}
    """
    word_freq = {}
    
    # Contar la frecuencia de cada palabra
    for word_list in words_list:
        for word in word_list:
            word_freq[word] = word_freq.get(word, 0) + 1
    
    # Ordenar el diccionario por valor en orden descendente
    sorted_word_freq = dict(sorted(word_freq.items(), key=lambda x: x[1], reverse=True))
    
    # Retornar las 5 principales (o todas si hay menos de 5)
    top_5 = dict(list(sorted_word_freq.items())[:5])
    
    return top_5