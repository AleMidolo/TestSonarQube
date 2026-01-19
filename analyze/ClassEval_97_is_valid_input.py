def is_valid_input(self, textnum):
    """
    जांचें कि इनपुट पाठ में केवल मान्य शब्द हैं जिन्हें संख्याओं में परिवर्तित किया जा सकता है।
    :param textnum: इनपुट पाठ जिसमें संख्याओं का प्रतिनिधित्व करने वाले शब्द हैं।
    :return: यदि इनपुट मान्य है तो True, अन्यथा False।
    >>> w2n = Words2Numbers()
    >>> w2n.is_valid_input("thirty-two")
    False
    """
    if not textnum or not isinstance(textnum, str):
        return False
    
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
    
    # Split by spaces and check each word
    words = textnum.split()
    
    for word in words:
        # Remove hyphens are not allowed based on the doctest
        if '-' in word:
            return False
        
        # Check if word is valid
        if word not in valid_words:
            return False
    
    return True