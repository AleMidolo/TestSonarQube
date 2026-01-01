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
    left = center - diff
    right = center + diff
    while left >= 0 and right < len(string) and (string[left] == string[right]):
        diff += 1
        left -= 1
        right += 1
    return diff - 1