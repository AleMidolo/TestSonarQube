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
        'billion', 'trillion', 'and', 'point', 'minus', 'negative'
    }
    
    # Clean and normalize the input
    textnum = textnum.lower().strip()
    
    # Remove extra spaces
    textnum = ' '.join(textnum.split())
    
    # Split by spaces and check each word
    words = textnum.split()
    
    for word in words:
        # Remove hyphens and check each part
        parts = word.split('-')
        for part in parts:
            if part and part not in valid_words:
                return False
    
    return True