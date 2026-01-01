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
        data = [data]
    average_precisions = []
    for sub_list, total_num in data:
        sub_list = np.array(sub_list)
        if total_num == 0:
            average_precisions.append(0.0)
            continue
        correct_count = 0
        precision_sum = 0.0
        for i, value in enumerate(sub_list):
            if value == 1:
                correct_count += 1
                precision_sum += correct_count / (i + 1)
        average_precision = precision_sum / min(correct_count, total_num)
        average_precisions.append(average_precision)
    return (np.mean(average_precisions), average_precisions)