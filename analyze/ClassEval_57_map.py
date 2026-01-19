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
    if type(data) != list and type(data) != tuple:
        raise Exception('the input must be a tuple([0,...,1,...],int) or a iteration of list of tuple')
    if len(data) == 0:
        return (0.0, [0.0])
    if type(data) == tuple:
        sub_list, total_num = data
        sub_list = np.array(sub_list)
        if total_num == 0:
            return (0.0, [0.0])
        relevant_positions = np.where(sub_list == 1)[0]
        if len(relevant_positions) == 0:
            ap = 0.0
        else:
            precisions = []
            relevant_count = 0
            for i, item in enumerate(sub_list):
                if item == 1:
                    relevant_count += 1
                    precision_at_i = relevant_count / (i + 1)
                    precisions.append(precision_at_i)
            ap = np.mean(precisions) if precisions else 0.0
        return (ap, [ap])
    if type(data) == list:
        separate_result = []
        for sub_list, total_num in data:
            sub_list = np.array(sub_list)
            if total_num == 0:
                ap = 0.0
            else:
                relevant_positions = np.where(sub_list == 1)[0]
                if len(relevant_positions) == 0:
                    ap = 0.0
                else:
                    precisions = []
                    relevant_count = 0
                    for i, item in enumerate(sub_list):
                        if item == 1:
                            relevant_count += 1
                            precision_at_i = relevant_count / (i + 1)
                            precisions.append(precision_at_i)
                    ap = np.mean(precisions) if precisions else 0.0
            separate_result.append(ap)
        return (np.mean(separate_result), separate_result)