class MetricsCalculator:
    def __init__(self):
        self.true_positives = 0
        self.false_positives = 0
        self.false_negatives = 0
        self.true_negatives = 0

    def update(self, predicted_labels, true_labels):
        for predicted, true in zip(predicted_labels, true_labels):
            self._update_metrics(predicted, true)

    def _update_metrics(self, predicted, true):
        if predicted == 1 and true == 1:
            self.true_positives += 1
        elif predicted == 1 and true == 0:
            self.false_positives += 1
        elif predicted == 0 and true == 1:
            self.false_negatives += 1
        elif predicted == 0 and true == 0:
            self.true_negatives += 1

    def precision(self, predicted_labels, true_labels):
        self.update(predicted_labels, true_labels)
        return self._calculate_precision()

    def _calculate_precision(self):
        if self.true_positives + self.false_positives == 0:
            return 0.0
        return self.true_positives / (self.true_positives + self.false_positives)

    def recall(self, predicted_labels, true_labels):
        self.update(predicted_labels, true_labels)
        return self._calculate_recall()

    def _calculate_recall(self):
        if self.true_positives + self.false_negatives == 0:
            return 0.0
        return self.true_positives / (self.true_positives + self.false_negatives)

    def f1_score(self, predicted_labels, true_labels):
        self.update(predicted_labels, true_labels)
        precision = self.precision(predicted_labels, true_labels)
        recall = self.recall(predicted_labels, true_labels)
        return self._calculate_f1_score(precision, recall)

    def _calculate_f1_score(self, precision, recall):
        if precision + recall == 0.0:
            return 0.0
        return (2 * precision * recall) / (precision + recall)

    def accuracy(self, predicted_labels, true_labels):
        self.update(predicted_labels, true_labels)
        return self._calculate_accuracy()

    def _calculate_accuracy(self):
        total = self.true_positives + self.true_negatives + self.false_positives + self.false_negatives
        if total == 0:
            return 0.0
        return (self.true_positives + self.true_negatives) / total