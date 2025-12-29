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
    if not data:
        return None
    count_dict = Counter(data)
    max_count = max(count_dict.values())
    if max_count == 1:
        return list(count_dict.keys())
    modes = [item for item, count in count_dict.items() if count == max_count]
    return sorted(modes)