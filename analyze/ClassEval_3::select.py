def select(self, m=None):
    """
        आंतरिक डेटा से m आइटम चुनकर व्यवस्थाओं की एक सूची उत्पन्न करता है।
        यदि m प्रदान नहीं किया गया है, तो सभी आइटम चुनता है।
        :param m: int, चुने जाने वाले आइटम की संख्या (डिफ़ॉल्ट=None)।
        :return: सूची, व्यवस्थाओं की एक सूची।
        >>> ac = ArrangementCalculator([1, 2, 3, 4])
        >>> ac.select(2)
        [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]]

        """
    if m is None:
        m = len(self.datas)
    return list(itertools.permutations(self.datas, m))