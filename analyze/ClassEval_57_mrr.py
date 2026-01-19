def mrr(data):
    """
    calcola l'MRR dei dati di input. L'MRR è un indice di valutazione ampiamente utilizzato. È la media del rango reciproco.
    :param data: i dati devono essere una tupla, lista 0,1, ad esempio ([1,0,...],5). In ogni tupla (risultato attuale, numero di verità di base), il numero di verità di base è il numero totale di verità di base.
     ([1,0,...],5),
    o lista di tuple ad esempio [([1,0,1,...],5),([1,0,...],6),([0,0,...],5)].
    1 rappresenta una risposta corretta, 0 rappresenta una risposta sbagliata.
    :return: se i dati di input sono una lista, restituisce il richiamo di questa lista. se i dati di input sono una lista di liste, restituisce la
    media del richiamo su tutte le liste. Il secondo valore di ritorno è una lista di precisione per ciascun input.
    >>> MetricsCalculator2.mrr(([1, 0, 1, 0], 4))
    >>> MetricsCalculator2.mrr([([1, 0, 1, 0], 4), ([0, 1, 0, 1], 4)])
    1.0, [1.0]
    0.75, [1.0, 0.5]
    """
    def calculate_single_mrr(results, ground_truth_count):
        # Find the rank of the first correct answer (1)
        for i, result in enumerate(results):
            if result == 1:
                # Rank is 1-indexed, so position i has rank i+1
                return 1.0 / (i + 1)
        # If no correct answer found, return 0
        return 0.0
    
    # Check if data is a single tuple or a list of tuples
    if isinstance(data, tuple):
        # Single tuple case
        results, ground_truth_count = data
        mrr_value = calculate_single_mrr(results, ground_truth_count)
        return mrr_value, [mrr_value]
    else:
        # List of tuples case
        mrr_values = []
        for results, ground_truth_count in data:
            mrr_value = calculate_single_mrr(results, ground_truth_count)
            mrr_values.append(mrr_value)
        
        # Calculate mean MRR
        mean_mrr = sum(mrr_values) / len(mrr_values) if mrr_values else 0.0
        return mean_mrr, mrr_values