def calculate_word_frequency(self, words_list):
    """
    शब्दों की सूची में प्रत्येक शब्द की शब्द आवृत्ति की गणना करें, और शब्द आवृत्ति शब्दकोश को मान के अनुसार अवरोही क्रम में क्रमबद्ध करें।
    :param words_list: शब्दों की सूचियों की एक सूची
    :return: शीर्ष 5 शब्द आवृत्ति शब्दकोश, एक शब्द आवृत्ति का शब्दकोश, कुंजी शब्द है, मान आवृत्ति है
    >>> NLPDataProcessor.calculate_word_frequency([['this', 'is', 'a', 'test'], ['this', 'is', 'another', 'test']])
    {'this': 2, 'is': 2, 'test': 2, 'a': 1, 'another': 1}
    """
    word_freq = {}
    
    # Count frequency of each word
    for word_list in words_list:
        for word in word_list:
            word_freq[word] = word_freq.get(word, 0) + 1
    
    # Sort by frequency in descending order, then by word alphabetically
    sorted_freq = dict(sorted(word_freq.items(), key=lambda x: (-x[1], x[0])))
    
    # Return top 5 items
    top_5 = dict(list(sorted_freq.items())[:5])
    
    return top_5