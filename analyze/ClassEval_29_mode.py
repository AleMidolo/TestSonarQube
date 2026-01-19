def mode(self, data):
    """
        डेटा के एक सेट का मोड कैलकुलेट करें।

        :param data: list, डेटा लिस्ट
        :return: float, मोड

        >>> ds = DataStatistics()
        >>> ds.mode([2, 2, 3, 3, 4])
        [2, 3]
        """
    count = Counter(data)
    max_freq = max(count.values())
    modes = [key for key, freq in count.items() if freq == max_freq]
    return modes