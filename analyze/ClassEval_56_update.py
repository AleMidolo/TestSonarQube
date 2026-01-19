def update(self, predicted_labels, true_labels):
    """
        Actualiza el número de las cuatro muestras (verdaderos_positivos, falsos_positivos, falsos_negativos, verdaderos_negativos)
        :param predicted_labels: lista, resultados predichos
        :param true_labels: lista, etiquetas verdaderas
        :return: Ninguno, cambia el número de muestras correspondientes
        >>> mc = MetricsCalculator()
        >>> mc.update([1, 1, 0, 0], [1, 0, 0, 1])
        (self.true_positives, self.false_positives, self.false_negatives, self.true_negatives) = (1, 1, 1, 1)
        """
    for pred, true in zip(predicted_labels, true_labels):
        if pred == 1 and true == 1:
            self.true_positives += 1
        elif pred == 1 and true == 0:
            self.false_positives += 1
        elif pred == 0 and true == 1:
            self.false_negatives += 1
        elif pred == 0 and true == 0:
            self.true_negatives += 1