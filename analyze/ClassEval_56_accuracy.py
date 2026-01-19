def accuracy(self, predicted_labels, true_labels):
    """
    Calcular la precisión
    :param predicted_labels: lista, resultados predichos
    :param true_labels: lista, etiquetas verdaderas
    :return: float
    >>> mc = MetricsCalculator()
    >>> mc.accuracy([1, 1, 0, 0], [1, 0, 0, 1])
    0.5
    """
    if len(predicted_labels) != len(true_labels):
        raise ValueError("Las listas deben tener la misma longitud")
    
    if len(predicted_labels) == 0:
        return 0.0
    
    correct = sum(1 for pred, true in zip(predicted_labels, true_labels) if pred == true)
    return correct / len(predicted_labels)