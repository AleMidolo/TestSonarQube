def median(data):
    """
    दी गई लिस्ट का मीडियन कैलकुलेट करता है।

    :param data: list, दी गई लिस्ट
    :return: float, दी गई लिस्ट का मीडियन

    >>> statistics3 = Statistics3()
    >>> statistics3.median([1, 2, 3, 4])
    2.5
    """
    if not data:
        return None
    
    sorted_data = sorted(data)
    n = len(sorted_data)
    
    if n % 2 == 0:
        # यदि लिस्ट की लंबाई सम है, तो बीच के दो तत्वों का औसत लें
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        return (mid1 + mid2) / 2
    else:
        # यदि लिस्ट की लंबाई विषम है, तो बीच का तत्व लें
        return float(sorted_data[n // 2])