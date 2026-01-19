def is_valid_input(self, textnum):
    """
    Controlla se il testo di input contiene solo parole valide che possono essere convertite in numeri.
    :param textnum: Il testo di input contenente parole che rappresentano numeri.
    :return: True se l'input è valido, False altrimenti.
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
        'billion', 'trillion', 'and', 'punto', 'virgola', 'point'
    }
    
    # Clean and normalize the input
    textnum = textnum.lower().strip()
    
    # If empty, it's not valid
    if not textnum:
        return False
    
    # Split by spaces and check each word
    words = textnum.split()
    
    for word in words:
        # Remove any trailing/leading whitespace
        word = word.strip()
        
        # Check if word contains hyphens (like "thirty-two")
        # According to the doctest, hyphenated words should return False
        if '-' in word:
            return False
        
        # Check if the word is in the valid words set
        if word not in valid_words:
            return False
    
    return True