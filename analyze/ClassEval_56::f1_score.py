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
    prec = self.precision(predicted_labels, true_labels)
    rec = self.recall(predicted_labels, true_labels)
    if prec + rec == 0:
        return 0.0
    return 2 * (prec * rec) / (prec + rec)