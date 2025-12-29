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
    modes = [key for key, value in count_dict.items() if value == max_count]
    return sorted(modes)