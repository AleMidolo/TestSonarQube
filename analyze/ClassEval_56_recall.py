def recall(self, predicted_labels, true_labels):
    """
    Calcular la recuperación
    :param predicted_labels: lista, resultados predichos
    :param true_labels: lista, etiquetas verdaderas
    :return: float
    >>> mc = MetricsCalculator()
    >>> mc.recall([1, 1, 0, 0], [1, 0, 0, 1])
    0.5
    """
    true_positives = sum(1 for pred, true in zip(predicted_labels, true_labels) if pred == 1 and true == 1)
    false_negatives = sum(1 for pred, true in zip(predicted_labels, true_labels) if pred == 0 and true == 1)
    
    if true_positives + false_negatives == 0:
        return 0.0
    
    return true_positives / (true_positives + false_negatives)