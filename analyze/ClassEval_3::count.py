class ArrangementCalculator: 
    def __init__(self, datas):
        """
        Initializes the ArrangementCalculator object with a list of datas.
        :param datas: List, the data elements to be used for arrangements.
        """
        self.datas = datas

    @staticmethod
    def count_all(n):
        """
            Counts the total number of all possible arrangements by choosing at least 1 item and at most n items from n items.
            :param n: int, the total number of items.
            :return: int, the count of all arrangements.
            >>> ArrangementCalculator.count_all(4)
            64
    
            """
    
        total = 0
        for i in range(1, n + 1):
            total += ArrangementCalculator.count(n, i)
        return total
    
    def select(self, m=None):
        """
        Generates a list of arrangements by selecting m items from the internal datas.
        If m is not provided, selects all items.
        :param m: int, the number of items to be chosen (default=None).
        :return: List, a list of arrangements.
        >>> ac = ArrangementCalculator([1, 2, 3, 4])
        >>> ac.select(2)
        [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]]
    
        """
    
        if m is None:
            m = len(self.datas)
        result = []
        for permutation in itertools.permutations(self.datas, m):
            result.append(list(permutation))
        return result
    
    def select_all(self):
        """
        Generates a list of all arrangements by selecting at least 1 item and at most the number of internal datas.
        :return: List, a list of all arrangements.
        >>> ac = ArrangementCalculator([1, 2, 3])
        >>> ac.select_all()
        [[1], [2], [3], [1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2], [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    
        """
    
        result = []
        for i in range(1, len(self.datas) + 1):
            result.extend(self.select(i))
        return result
    
    @staticmethod
    def factorial(n):
        """
            Calculates the factorial of a given number.
            :param n: int, the number to calculate the factorial.
            :return: int, the factorial of the given number.
            >>> ArrangementCalculator.factorial(4)
            24
    
            """
    
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def count(n, m=None):
        """
        n आइटम में से m आइटम चुनकर व्यवस्थाओं की संख्या गिनता है (परम्यूटेशन)।
        यदि m प्रदान नहीं किया गया है या n, m के बराबर है, तो factorial(n) लौटाता है।
        :param n: int, आइटम की कुल संख्या।
        :param m: int, चुने जाने वाले आइटम की संख्या (डिफ़ॉल्ट=None)।
        :return: int, व्यवस्थाओं की संख्या।
        >>> ArrangementCalculator.count(5, 3)
        60

        """
        if m is None or n == m:
            return ArrangementCalculator.factorial(n)
        return ArrangementCalculator.factorial(n) // ArrangementCalculator.factorial(n - m)