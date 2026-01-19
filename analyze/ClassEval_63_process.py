def process(self, string_list):
    """
    keep only English letters and spaces in the string, then convert the string to lower case, and then split the string into a list of words. Calculate the word frequency of each word in the list of words list, and sort the word frequency dictionary by value in descending order.
    :param string_list: a list of strings
    :return: top 5 word frequency dictionary, a dictionary of word frequency, key is word, value is frequency
    >>> NLPDataProcessor.process(['This is a test.', 'This is another test.'])
    {'this': 2, 'is': 2, 'test': 2, 'a': 1, 'another': 1}
    """
    import re
    from collections import Counter
    
    # Process all strings
    all_words = []
    for string in string_list:
        # Keep only English letters and spaces
        cleaned = re.sub(r'[^a-zA-Z\s]', '', string)
        # Convert to lower case
        cleaned = cleaned.lower()
        # Split into words
        words = cleaned.split()
        all_words.extend(words)
    
    # Calculate word frequency
    word_freq = Counter(all_words)
    
    # Sort by frequency in descending order and get top 5
    sorted_freq = dict(sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:5])
    
    return sorted_freq