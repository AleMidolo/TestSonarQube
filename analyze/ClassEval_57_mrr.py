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
    def calculate_single_mrr(result_list, ground_truth):
        # MRR es el recíproco del rango de la primera respuesta correcta
        for i, val in enumerate(result_list):
            if val == 1:
                return 1.0 / (i + 1)  # i+1 porque el rango comienza en 1
        return 0.0  # Si no hay respuestas correctas
    
    # Verificar si data es una sola tupla o una lista de tuplas
    if isinstance(data, tuple):
        # Caso de una sola tupla
        result_list, ground_truth = data
        mrr_value = calculate_single_mrr(result_list, ground_truth)
        return mrr_value, [mrr_value]
    else:
        # Caso de lista de tuplas
        mrr_list = []
        for result_list, ground_truth in data:
            mrr_value = calculate_single_mrr(result_list, ground_truth)
            mrr_list.append(mrr_value)
        
        # Calcular el promedio de MRR
        avg_mrr = sum(mrr_list) / len(mrr_list) if mrr_list else 0.0
        return avg_mrr, mrr_list