def is_valid_input(self, textnum):
    """
    Verifica si el texto de entrada contiene solo palabras válidas que se pueden convertir en números.
    :param textnum: El texto de entrada que contiene palabras que representan números.
    :return: True si la entrada es válida, False en caso contrario.
    >>> w2n = Words2Numbers()
    >>> w2n.is_valid_input("thirty-two")
    False
    """
    # Define valid number words
    valid_words = {
        'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
        'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
        'seventeen', 'eighteen', 'nineteen', 'twenty', 'thirty', 'forty', 'fifty',
        'sixty', 'seventy', 'eighty', 'ninety', 'hundred', 'thousand', 'million',
        'billion', 'trillion', 'and', 'point'
    }
    
    # Clean and normalize the input
    textnum = textnum.lower().strip()
    
    # If empty, it's not valid
    if not textnum:
        return False
    
    # Split by spaces and hyphens
    words = textnum.replace('-', ' ').split()
    
    # Check if all words are valid
    for word in words:
        if word not in valid_words:
            return False
    
    return True