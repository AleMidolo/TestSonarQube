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
    
    if type(data) != list and type(data) != tuple:
        raise Exception(
                "the input must be a tuple([0,...,1,...],int) or a iteration of list of tuple")

    if len(data) == 0:
        return 0.0, [0.0]
    
    if type(data) == tuple:
        (sub_list, total_num) = data
        if total_num == 0:
            return 0.0, [0.0]
        else:
            rank = next((i + 1 for i, val in enumerate(sub_list) if val == 1), None)
            mrr = 1.0 / rank if rank is not None else 0.0
            return mrr, [mrr]

    if type(data) == list:
        separate_result = []
        for (sub_list, total_num) in data:
            if total_num == 0:
                mrr = 0.0
            else:
                rank = next((i + 1 for i, val in enumerate(sub_list) if val == 1), None)
                mrr = 1.0 / rank if rank is not None else 0.0

            separate_result.append(mrr)
        return np.mean(separate_result), separate_result