def process(self, string_list):
    """
    mantiene solo le lettere inglesi e gli spazi nella stringa, quindi converte la stringa in minuscolo, e poi divide la stringa in una lista di parole. Calcola la frequenza delle parole di ciascuna parola nella lista di parole e ordina il dizionario della frequenza delle parole per valore in ordine decrescente.
    :param string_list: una lista di stringhe
    :return: dizionario della frequenza delle parole top 5, un dizionario della frequenza delle parole, la chiave è la parola, il valore è la frequenza
    >>> NLPDataProcessor.process(['This is a test.', 'This is another test.'])
    {'this': 2, 'is': 2, 'test': 2, 'a': 1, 'another': 1}
    """
    import re
    from collections import Counter
    
    # Combina tutte le stringhe in una sola
    combined_string = ' '.join(string_list)
    
    # Mantiene solo lettere inglesi e spazi
    cleaned_string = re.sub(r'[^a-zA-Z\s]', '', combined_string)
    
    # Converte in minuscolo
    lowercase_string = cleaned_string.lower()
    
    # Divide in parole
    words = lowercase_string.split()
    
    # Calcola la frequenza delle parole
    word_freq = Counter(words)
    
    # Ordina per frequenza in ordine decrescente e prende i top 5
    sorted_freq = dict(sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:5])
    
    return sorted_freq