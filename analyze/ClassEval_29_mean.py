def mean(self, data):
    """
        डेटा के ग्रुप की एवरेज वैल्यू कैलकुलेट करें, जो डेसिमल सेपरेटर के बाद दो डिजिट तक एक्यूरेट हो।

        :param data: list, डेटा लिस्ट
        :return: float, मीन वैल्यू

        >>> ds = DataStatistics()
        >>> ds.mean([1, 2, 3, 4, 5])
        3.00
        """
    return round(sum(data) / len(data), 2)