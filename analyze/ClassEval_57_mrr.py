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
    def calculate_single_rr(result_list, ground_truth_count):
        # Find the rank of the first correct answer (1)
        for i, val in enumerate(result_list):
            if val == 1:
                # Rank is 1-indexed, so position 0 has rank 1
                return 1.0 / (i + 1)
        # If no correct answer found, reciprocal rank is 0
        return 0.0
    
    # Check if data is a single tuple or a list of tuples
    if isinstance(data, tuple):
        # Single tuple case
        result_list, ground_truth_count = data
        rr = calculate_single_rr(result_list, ground_truth_count)
        return rr, [rr]
    else:
        # List of tuples case
        rr_list = []
        for result_list, ground_truth_count in data:
            rr = calculate_single_rr(result_list, ground_truth_count)
            rr_list.append(rr)
        
        # Calculate mean reciprocal rank
        mean_rr = sum(rr_list) / len(rr_list) if rr_list else 0.0
        return mean_rr, rr_list