def process(self, string_list):
    """
        mantener solo letras en inglés y espacios en la cadena, luego convertir la cadena a minúsculas, y luego dividir la cadena en una lista de palabras. Calcular la frecuencia de cada palabra en la lista de palabras, y ordenar el diccionario de frecuencia de palabras por valor en orden descendente.
        :param string_list: una lista de cadenas
        :return: diccionario de frecuencia de palabras de las 5 principales, un diccionario de frecuencia de palabras, la clave es la palabra, el valor es la frecuencia
        >>> NLPDataProcessor2().process(['This is a test.', 'This is another test.'])
        {'this': 2, 'is': 2, 'test': 2, 'a': 1, 'another': 1}
        """
    words_list = self.process_data(string_list)
    return self.calculate_word_frequency(words_list)