def f1_score(self, predicted_labels, true_labels):
    """
        Calcola il punteggio f1, che è la media armonica di precisione e richiamo
        :param predicted_labels: lista, risultati previsti
        :param true_labels: lista, etichette vere
        :return: float
        >>> mc = MetricsCalculator()
        >>> mc.f1_score([1, 1, 0, 0], [1, 0, 0, 1])
        0.5
        """
    prec = self.precision(predicted_labels, true_labels)
    rec = self.recall(predicted_labels, true_labels)
    if prec + rec == 0:
        return 0.0
    return 2 * (prec * rec) / (prec + rec)