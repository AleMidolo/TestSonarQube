def is_valid_input(self, textnum):
    """
    Verifica si el texto de entrada contiene solo palabras válidas que se pueden convertir en números.
    :param textnum: El texto de entrada que contiene palabras que representan números.
    :return: True si la entrada es válida, False en caso contrario.
    >>> w2n = Words2Numbers()
    >>> w2n.is_valid_input("thirty-two")
    False
    """
    if not textnum or not isinstance(textnum, str):
        return False
    
    # Definir palabras válidas para números
    valid_words = {
        'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
        'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
        'seventeen', 'eighteen', 'nineteen', 'twenty', 'thirty', 'forty', 'fifty',
        'sixty', 'seventy', 'eighty', 'ninety', 'hundred', 'thousand', 'million',
        'billion', 'trillion', 'and', 'point', 'minus', 'negative'
    }
    
    # Limpiar y normalizar el texto
    text = textnum.lower().strip()
    
    # Reemplazar guiones con espacios para separar palabras compuestas
    text = text.replace('-', ' ')
    
    # Dividir en palabras
    words = text.split()
    
    # Verificar que todas las palabras sean válidas
    for word in words:
        if word and word not in valid_words:
            return False
    
    return True