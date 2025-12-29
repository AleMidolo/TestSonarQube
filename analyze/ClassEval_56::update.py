def update(self, predicted_labels, true_labels):
    """
        Aggiorna il numero di tutti e quattro i campioni (veri_positivi, falsi_positivi, falsi_negativi, veri_negativi)
        :param predicted_labels: lista, risultati previsti
        :param true_labels: lista, etichette vere
        :return: None, modifica il numero dei campioni corrispondenti
        >>> mc = MetricsCalculator()
        >>> mc.update([1, 1, 0, 0], [1, 0, 0, 1])
        (self.true_positives, self.false_positives, self.false_negatives, self.true_negatives) = (1, 1, 1, 1)
        """
    self.true_positives = 0
    self.false_positives = 0
    self.false_negatives = 0
    self.true_negatives = 0
    for pred, true in zip(predicted_labels, true_labels):
        if pred == 1 and true == 1:
            self.true_positives += 1
        elif pred == 1 and true == 0:
            self.false_positives += 1
        elif pred == 0 and true == 1:
            self.false_negatives += 1
        elif pred == 0 and true == 0:
            self.true_negatives += 1