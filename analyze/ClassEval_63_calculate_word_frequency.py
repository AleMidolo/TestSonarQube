def calculate_word_frequency(self, words_list):
    """
    Calculate the word frequency of each word in the list of words list, and sort the word frequency dictionary by value in descending order.
    :param words_list: a list of words lists
    :return: top 5 word frequency dictionary, a dictionary of word frequency, key is word, value is frequency
    >>> NLPDataProcessor.calculate_word_frequency([['this', 'is', 'a', 'test'], ['this', 'is', 'another', 'test']])
    {'this': 2, 'is': 2, 'test': 2, 'a': 1, 'another': 1}
    """
    word_freq = {}
    
    # Count frequency of each word across all lists
    for word_list in words_list:
        for word in word_list:
            word_freq[word] = word_freq.get(word, 0) + 1
    
    # Sort by frequency in descending order, then by word alphabetically for ties
    sorted_word_freq = dict(sorted(word_freq.items(), key=lambda x: (-x[1], x[0])))
    
    # Return top 5 items
    top_5 = dict(list(sorted_word_freq.items())[:5])
    
    return top_5