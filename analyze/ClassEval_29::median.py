def median(self, data):
    """
        डेसिमल सेपरेटर के बाद दो डिजिट तक सटीक, डेटा के ग्रुप का मीडियन कैलकुलेट करें।

        :param data: list, डेटा लिस्ट
        :return: float, मीडियन वैल्यू

        >>> ds = DataStatistics()
        >>> ds.median([2, 5, 1, 3, 4])
        3.00
        """
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return round((sorted_data[mid - 1] + sorted_data[mid]) / 2, 2)
    else:
        return round(sorted_data[mid], 2)