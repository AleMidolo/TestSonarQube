def calculate_word_frequency(self, words_list):
    """
        Calculate the word frequency of each word in the list of words list, and sort the word frequency dictionary by value in descending order.
        :param words_list: a list of words lists
        :return: top 5 word frequency dictionary, a dictionary of word frequency, key is word, value is frequency
        >>> NLPDataProcessor2.calculate_word_frequency([['this', 'is', 'a', 'test'], ['this', 'is', 'another', 'test']])
        {'this': 2, 'is': 2, 'test': 2, 'a': 1, 'another': 1}
        """
    flat_list = [word for sublist in words_list for word in sublist]
    word_count = Counter(flat_list)
    return dict(word_count.most_common(5))