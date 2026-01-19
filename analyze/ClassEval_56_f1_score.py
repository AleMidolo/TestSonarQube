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
    self.update(predicted_labels, true_labels)
    precision = self.precision(predicted_labels, true_labels)
    recall = self.recall(predicted_labels, true_labels)
    if precision + recall == 0:
        return 0.0
    return 2 * (precision * recall) / (precision + recall)