def calculate_word_frequency(self, words_list):
    """
        Calcola la frequenza delle parole di ciascuna parola nella lista di liste di parole e ordina il dizionario della frequenza delle parole per valore in ordine decrescente.
        :param words_list: una lista di liste di parole
        :return: dizionario della frequenza delle parole top 5, un dizionario della frequenza delle parole, la chiave è la parola, il valore è la frequenza
        >>> NLPDataProcessor2().calculate_word_frequency([['this', 'is', 'a', 'test'], ['this', 'is', 'another', 'test']])
        {'this': 2, 'is': 2, 'test': 2, 'a': 1, 'another': 1}
        """
    word_counter = Counter()
    for words in words_list:
        word_counter.update(words)
    sorted_items = sorted(word_counter.items(), key=lambda x: x[1], reverse=True)
    top_5 = dict(sorted_items[:5])
    return top_5