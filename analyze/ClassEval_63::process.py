def process(self, string_list):
    """
        mantiene solo le lettere inglesi e gli spazi nella stringa, quindi converte la stringa in minuscolo, e poi divide la stringa in una lista di parole. Calcola la frequenza delle parole di ciascuna parola nella lista di parole e ordina il dizionario della frequenza delle parole per valore in ordine decrescente.
        :param string_list: una lista di stringhe
        :return: dizionario della frequenza delle parole top 5, un dizionario della frequenza delle parole, la chiave è la parola, il valore è la frequenza
        >>> NLPDataProcessor2.process(['This is a test.', 'This is another test.'])
        {'this': 2, 'is': 2, 'test': 2, 'a': 1, 'another': 1}
        """
    words_list = self.process_data(string_list)
    return self.calculate_word_frequency(words_list)