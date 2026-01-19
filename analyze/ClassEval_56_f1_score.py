def f1_score(self, predicted_labels, true_labels):
    """
    Calcular la puntuación f1, que es la media armónica de la precisión y el recall
    :param predicted_labels: lista, resultados predichos
    :param true_labels: lista, etiquetas verdaderas
    :return: float
    >>> mc = MetricsCalculator()
    >>> mc.f1_score([1, 1, 0, 0], [1, 0, 0, 1])
    0.5
    """
    # Calculate True Positives, False Positives, and False Negatives
    tp = sum(1 for pred, true in zip(predicted_labels, true_labels) if pred == 1 and true == 1)
    fp = sum(1 for pred, true in zip(predicted_labels, true_labels) if pred == 1 and true == 0)
    fn = sum(1 for pred, true in zip(predicted_labels, true_labels) if pred == 0 and true == 1)
    
    # Calculate precision
    if tp + fp == 0:
        precision = 0
    else:
        precision = tp / (tp + fp)
    
    # Calculate recall
    if tp + fn == 0:
        recall = 0
    else:
        recall = tp / (tp + fn)
    
    # Calculate F1 score (harmonic mean of precision and recall)
    if precision + recall == 0:
        return 0.0
    else:
        f1 = 2 * (precision * recall) / (precision + recall)
        return f1