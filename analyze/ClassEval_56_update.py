def update(self, predicted_labels, true_labels):
    """
        सभी चार नमूनों (सच्चे सकारात्मक, झूठे सकारात्मक, झूठे नकारात्मक, सच्चे नकारात्मक) की संख्या को अपडेट करें
        :param predicted_labels: सूची, पूर्वानुमानित परिणाम
        :param true_labels: सूची, सच्चे लेबल
        :return: None, संबंधित नमूनों की संख्या में परिवर्तन करें
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