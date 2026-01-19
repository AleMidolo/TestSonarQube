def calculate_word_frequency(self, words_list):
    """
    Calcola la frequenza delle parole di ciascuna parola nella lista di liste di parole e ordina il dizionario della frequenza delle parole per valore in ordine decrescente.
    :param words_list: una lista di liste di parole
    :return: dizionario della frequenza delle parole top 5, un dizionario della frequenza delle parole, la chiave è la parola, il valore è la frequenza
    >>> NLPDataProcessor.calculate_word_frequency([['this', 'is', 'a', 'test'], ['this', 'is', 'another', 'test']])
    {'this': 2, 'is': 2, 'test': 2, 'a': 1, 'another': 1}
    """
    word_freq = {}
    
    # Flatten the list of lists and count word frequencies
    for word_list in words_list:
        for word in word_list:
            word_freq[word] = word_freq.get(word, 0) + 1
    
    # Sort the dictionary by value in descending order, then by key alphabetically for ties
    sorted_word_freq = dict(sorted(word_freq.items(), key=lambda item: (-item[1], item[0])))
    
    # Return top 5 items
    top_5 = dict(list(sorted_word_freq.items())[:5])
    
    return top_5