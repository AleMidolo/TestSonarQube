@staticmethod
def map(data):
    """
        calcula el MAP de los datos de entrada. MAP es un índice de evaluación ampliamente utilizado. Es la media de AP (precisión promedio).
        :param data: los datos deben ser una tupla, lista 0,1, ej. ([1,0,...],5). En cada tupla (resultado actual, número de verdad fundamental), el número de verdad fundamental es el total de números de verdad.
        ([1,0,...],5),
        o lista de tuplas ej. [([1,0,1,...],5),([1,0,...],6),([0,0,...],5)].
        1 representa una respuesta correcta, 0 representa una respuesta incorrecta.
        :return: si los datos de entrada son una lista, devuelve el recall de esta lista. si los datos de entrada son una lista de listas, devuelve el
        recall promedio en todas las listas. El segundo valor de retorno es una lista de precisión para cada entrada.
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
        relevant_positions = np.where(sub_list == 1)[0] + 1
        if len(relevant_positions) == 0:
            ap = 0.0
        else:
            precisions = []
            for k in range(1, len(sub_list) + 1):
                relevant_at_k = np.sum(sub_list[:k])
                precision_at_k = relevant_at_k / k if k > 0 else 0.0
                if sub_list[k - 1] == 1:
                    precisions.append(precision_at_k)
            if len(precisions) > 0:
                ap = np.mean(precisions)
            else:
                ap = 0.0
        return (ap, [ap])
    if type(data) == list:
        separate_result = []
        for sub_list, total_num in data:
            sub_list = np.array(sub_list)
            if total_num == 0:
                ap = 0.0
            else:
                relevant_positions = np.where(sub_list == 1)[0] + 1
                if len(relevant_positions) == 0:
                    ap = 0.0
                else:
                    precisions = []
                    for k in range(1, len(sub_list) + 1):
                        relevant_at_k = np.sum(sub_list[:k])
                        precision_at_k = relevant_at_k / k if k > 0 else 0.0
                        if sub_list[k - 1] == 1:
                            precisions.append(precision_at_k)
                    if len(precisions) > 0:
                        ap = np.mean(precisions)
                    else:
                        ap = 0.0
            separate_result.append(ap)
        map_score = np.mean(separate_result) if len(separate_result) > 0 else 0.0
        return (map_score, separate_result)