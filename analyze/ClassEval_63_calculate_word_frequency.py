def calculate_word_frequency(self, words_list):
    """
        Calcola la frequenza delle parole di ciascuna parola nella lista di liste di parole e ordina il dizionario della frequenza delle parole per valore in ordine decrescente.
        :param words_list: una lista di liste di parole
        :return: dizionario della frequenza delle parole top 5, un dizionario della frequenza delle parole, la chiave è la parola, il valore è la frequenza
        >>> NLPDataProcessor2().calculate_word_frequency([['this', 'is', 'a', 'test'], ['this', 'is', 'another', 'test']])
        {'this': 2, 'is': 2, 'test': 2, 'a': 1, 'another': 1}
        """
    all_words = []
    for sublist in words_list:
        all_words.extend(sublist)
    word_counts = Counter(all_words)
    sorted_items = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    top_5_items = sorted_items[:5]
    top_5_dict = dict(top_5_items)
    return top_5_dict