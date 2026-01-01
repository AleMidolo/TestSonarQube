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
    self.update(predicted_labels, true_labels)
    total_correct = self.true_positives + self.true_negatives
    total_samples = len(predicted_labels)
    if total_samples == 0:
        return 0.0
    return total_correct / total_samples