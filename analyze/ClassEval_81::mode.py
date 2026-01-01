@staticmethod
def mode(data):
    """
        दी गई लिस्ट का मोड कैलकुलेट करता है।

        :param data: list, दी गई लिस्ट
        :return: list, दी गई लिस्ट का मोड

        >>> statistics3 = Statistics3()
        >>> statistics3.mode([1, 2, 3, 3])
        [3]
        """
    from collections import Counter
    if not data:
        return []
    count = Counter(data)
    max_count = max(count.values())
    return [num for num, freq in count.items() if freq == max_count]