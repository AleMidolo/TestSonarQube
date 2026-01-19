def mrr(data):
    """
        calcula el MRR de los datos de entrada. MRR es un índice de evaluación ampliamente utilizado. Es la media del rango recíproco.
        :param data: los datos deben ser una tupla, lista 0,1, ej. ([1,0,...],5). En cada tupla (resultado real, número de verdad fundamental), el número de verdad fundamental es el total de números de verdad.
         ([1,0,...],5),
        o lista de tuplas ej. [([1,0,1,...],5),([1,0,...],6),([0,0,...],5)].
        1 representa una respuesta correcta, 0 representa una respuesta incorrecta.
        :return: si los datos de entrada son una lista, devuelve el recall de esta lista. si los datos de entrada son una lista de listas, devuelve el
        recall promedio en todas las listas. El segundo valor de retorno es una lista de precisión para cada entrada.
        >>> MetricsCalculator2.mrr(([1, 0, 1, 0], 4))
        >>> MetricsCalculator2.mrr([([1, 0, 1, 0], 4), ([0, 1, 0, 1], 4)])
        1.0, [1.0]
        0.75, [1.0, 0.5]
        """
    if type(data) != list and type(data) != tuple:
        raise Exception('the input must be a tuple([0,...,1,...],int) or a iteration of list of tuple')
    if len(data) == 0:
        return (0.0, [0.0])
    if type(data) == tuple:
        sub_list, total_num = data
        if total_num == 0:
            return (0.0, [0.0])
        else:
            rank = next((i + 1 for i, val in enumerate(sub_list) if val == 1), None)
            mrr_value = 1.0 / rank if rank is not None else 0.0
            return (mrr_value, [mrr_value])
    if type(data) == list:
        separate_result = []
        for sub_list, total_num in data:
            if total_num == 0:
                mrr_value = 0.0
            else:
                rank = next((i + 1 for i, val in enumerate(sub_list) if val == 1), None)
                mrr_value = 1.0 / rank if rank is not None else 0.0
            separate_result.append(mrr_value)
        return (np.mean(separate_result), separate_result)