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
        'billion', 'trillion', 'and'
    }
    
    # Clean and split the input text
    textnum = textnum.strip().lower()
    
    # If empty, it's not valid
    if not textnum:
        return False
    
    # Split by spaces and check each word
    words = textnum.split()
    
    for word in words:
        # Remove any non-alphabetic characters for checking
        clean_word = ''.join(c for c in word if c.isalpha())
        if clean_word and clean_word not in valid_words:
            return False
    
    return True