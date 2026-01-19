def precision(self, predicted_labels, true_labels):
    """
    Calcular precisión
    :param predicted_labels: lista, resultados predichos
    :param true_labels: lista, etiquetas verdaderas
    :return: float
    >>> mc = MetricsCalculator()
    >>> mc.precision([1, 1, 0, 0], [1, 0, 0, 1])
    0.5
    """
    true_positives = sum(1 for pred, true in zip(predicted_labels, true_labels) if pred == 1 and true == 1)
    false_positives = sum(1 for pred, true in zip(predicted_labels, true_labels) if pred == 1 and true == 0)
    
    if true_positives + false_positives == 0:
        return 0.0
    
    return true_positives / (true_positives + false_positives)