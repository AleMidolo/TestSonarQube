def process(self, string_list):
    """
    mantener solo letras en inglés y espacios en la cadena, luego convertir la cadena a minúsculas, y luego dividir la cadena en una lista de palabras. Calcular la frecuencia de cada palabra en la lista de palabras, y ordenar el diccionario de frecuencia de palabras por valor en orden descendente.
    :param string_list: una lista de cadenas
    :return: diccionario de frecuencia de palabras de las 5 principales, un diccionario de frecuencia de palabras, la clave es la palabra, el valor es la frecuencia
    >>> NLPDataProcessor.process(['This is a test.', 'This is another test.'])
    {'this': 2, 'is': 2, 'test': 2, 'a': 1, 'another': 1}
    """
    import re
    from collections import Counter
    
    # Procesar todas las cadenas
    all_words = []
    
    for string in string_list:
        # Mantener solo letras en inglés y espacios
        cleaned_string = re.sub(r'[^a-zA-Z\s]', '', string)
        
        # Convertir a minúsculas
        lowercase_string = cleaned_string.lower()
        
        # Dividir en palabras
        words = lowercase_string.split()
        
        # Agregar palabras a la lista total
        all_words.extend(words)
    
    # Calcular frecuencia de cada palabra
    word_freq = Counter(all_words)
    
    # Ordenar por frecuencia en orden descendente y tomar las 5 principales
    sorted_freq = dict(sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:5])
    
    return sorted_freq