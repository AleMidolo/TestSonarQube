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
    def calculate_ap(predictions, ground_truth_count):
        """Calculate Average Precision for a single query"""
        if ground_truth_count == 0:
            return 0.0
        
        ap = 0.0
        correct_count = 0
        
        for i, pred in enumerate(predictions):
            if pred == 1:
                correct_count += 1
                precision_at_i = correct_count / (i + 1)
                ap += precision_at_i
        
        return ap / ground_truth_count
    
    # Check if data is a single tuple or a list of tuples
    if isinstance(data, tuple):
        # Single query case
        predictions, ground_truth_count = data
        ap = calculate_ap(predictions, ground_truth_count)
        return ap, [ap]
    else:
        # Multiple queries case
        ap_list = []
        for predictions, ground_truth_count in data:
            ap = calculate_ap(predictions, ground_truth_count)
            ap_list.append(ap)
        
        mean_ap = sum(ap_list) / len(ap_list) if ap_list else 0.0
        return mean_ap, ap_list