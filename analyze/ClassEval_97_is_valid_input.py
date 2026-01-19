def is_valid_input(self, textnum):
    """
    जांचें कि इनपुट पाठ में केवल मान्य शब्द हैं जिन्हें संख्याओं में परिवर्तित किया जा सकता है।
    :param textnum: इनपुट पाठ जिसमें संख्याओं का प्रतिनिधित्व करने वाले शब्द हैं।
    :return: यदि इनपुट मान्य है तो True, अन्यथा False।
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
    
    # Convert to lowercase and split by spaces
    textnum = textnum.lower().strip()
    
    # Split by spaces to get individual words
    words = textnum.split()
    
    # Check each word
    for word in words:
        # Remove any hyphens and check each part
        # If word contains hyphen, it's invalid based on the doctest
        if '-' in word:
            return False
        
        # Check if word is in valid words
        if word not in valid_words:
            return False
    
    return True