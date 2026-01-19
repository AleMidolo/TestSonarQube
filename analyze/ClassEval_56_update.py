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
    tp = fp = fn = tn = 0
    for pred, true in zip(predicted_labels, true_labels):
        if pred == 1 and true == 1:
            tp += 1
        elif pred == 1 and true == 0:
            fp += 1
        elif pred == 0 and true == 1:
            fn += 1
        elif pred == 0 and true == 0:
            tn += 1
    self.true_positives = tp
    self.false_positives = fp
    self.false_negatives = fn
    self.true_negatives = tn