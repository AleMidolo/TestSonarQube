def is_valid_input(self, textnum):
    """
    Check if the input text contains only valid words that can be converted into numbers.
    :param textnum: The input text containing words representing numbers.
    :return: True if input is valid, False otherwise.
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
    
    # Replace hyphens with spaces to split hyphenated words
    textnum = textnum.replace('-', ' ')
    
    # Split into words
    words = textnum.split()
    
    # Check if all words are valid
    for word in words:
        if word and word not in valid_words:
            return False
    
    return True