def median(self, data):
    """
    डेसिमल सेपरेटर के बाद दो डिजिट तक सटीक, डेटा के ग्रुप का मीडियन कैलकुलेट करें।

    :param data: list, डेटा लिस्ट
    :return: float, मीडियन वैल्यू

    >>> ds = DataStatistics()
    >>> ds.median([2, 5, 1, 3, 4])
    3.00
    """
    if not data:
        return 0.00
    
    sorted_data = sorted(data)
    n = len(sorted_data)
    
    if n % 2 == 1:
        # Odd number of elements - return middle element
        median_value = sorted_data[n // 2]
    else:
        # Even number of elements - return average of two middle elements
        median_value = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    
    return round(median_value, 2)