def mode(self, data):
    """
        डेटा के एक सेट का मोड कैलकुलेट करें।

        :param data: list, डेटा लिस्ट
        :return: float, मोड

        >>> ds = DataStatistics()
        >>> ds.mode([2, 2, 3, 3, 4])
        [2, 3]
        """
    if not data:
        return []
    counter = Counter(data)
    max_count = max(counter.values())
    modes = [key for key, count in counter.items() if count == max_count]
    return sorted(modes)