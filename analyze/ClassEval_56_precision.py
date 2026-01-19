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
    self.update(predicted_labels, true_labels)
    if self.true_positives + self.false_positives == 0:
        return 0.0
    return self.true_positives / (self.true_positives + self.false_positives)