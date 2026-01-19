@staticmethod
def map(data):
    """
    calcola il MAP dei dati di input. MAP è un indice di valutazione ampiamente utilizzato. È la media di AP (precisione media).
    :param data: i dati devono essere una tupla, lista 0,1, ad esempio ([1,0,...],5). In ogni tupla (risultato attuale, numero di verità di base), il numero di verità di base è il numero totale di verità di base.
    ([1,0,...],5),
    oppure una lista di tuple ad esempio [([1,0,1,...],5),([1,0,...],6),([0,0,...],5)].
    1 rappresenta una risposta corretta, 0 rappresenta una risposta sbagliata.
    :return: se i dati di input sono una lista, restituisce il richiamo di questa lista. se i dati di input sono una lista di liste, restituisce la
    media del richiamo su tutte le liste. Il secondo valore di ritorno è una lista di precisione per ciascun input.
    >>> MetricsCalculator2.map(([1, 0, 1, 0], 4))
    >>> MetricsCalculator2.map([([1, 0, 1, 0], 4), ([0, 1, 0, 1], 4)])
    0.41666666666666663, [0.41666666666666663]
    0.3333333333333333, [0.41666666666666663, 0.25]
    """
    def calculate_ap(results, ground_truth_count):
        """Calculate Average Precision for a single query"""
        if ground_truth_count == 0:
            return 0.0
        
        correct_count = 0
        precision_sum = 0.0
        
        for i, result in enumerate(results):
            if result == 1:
                correct_count += 1
                precision_at_k = correct_count / (i + 1)
                precision_sum += precision_at_k
        
        ap = precision_sum / ground_truth_count
        return ap
    
    # Check if data is a single tuple or a list of tuples
    if isinstance(data, tuple):
        # Single query case
        results, ground_truth_count = data
        ap = calculate_ap(results, ground_truth_count)
        return ap, [ap]
    else:
        # Multiple queries case
        ap_list = []
        for results, ground_truth_count in data:
            ap = calculate_ap(results, ground_truth_count)
            ap_list.append(ap)
        
        mean_ap = sum(ap_list) / len(ap_list) if ap_list else 0.0
        return mean_ap, ap_list