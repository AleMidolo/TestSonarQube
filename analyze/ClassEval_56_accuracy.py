def accuracy(self, predicted_labels, true_labels):
    """
    Calcola l'accuratezza
    :param predicted_labels: lista, risultati previsti
    :param true_labels: lista, etichette vere
    :return: float
    >>> mc = MetricsCalculator()
    >>> mc.accuracy([1, 1, 0, 0], [1, 0, 0, 1])
    0.5
    """
    if len(predicted_labels) != len(true_labels):
        raise ValueError("Le liste devono avere la stessa lunghezza")
    
    if len(predicted_labels) == 0:
        return 0.0
    
    correct = sum(1 for pred, true in zip(predicted_labels, true_labels) if pred == true)
    return correct / len(predicted_labels)