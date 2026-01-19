def palindromic_length(self, center, diff, string):
    """
    दिए गए केंद्र, अंतर मान, और इनपुट स्ट्रिंग के आधार पर पलिंड्रोमिक उपस्ट्रिंग की लंबाई को पुनरावृत्तिपूर्वक गणना करता है।
    :param center: पलिंड्रोमिक उपस्ट्रिंग का केंद्र, int.
    :param diff: केंद्र और वर्तमान स्थिति के बीच का अंतर, int.
    :param string: खोजी जाने वाली स्ट्रिंग, str.
    :return: पलिंड्रोमिक उपस्ट्रिंग की लंबाई, int.
    >>> manacher = Manacher('ababa')
    >>> manacher.palindromic_length(2, 1, 'a|b|a|b|a')
    2

    """
    # Base case: if diff goes out of bounds
    if center - diff < 0 or center + diff >= len(string):
        return 0
    
    # If characters at center-diff and center+diff match
    if string[center - diff] == string[center + diff]:
        # Recursively check the next positions
        return 1 + self.palindromic_length(center, diff + 1, string)
    else:
        # Characters don't match, stop expanding
        return 0