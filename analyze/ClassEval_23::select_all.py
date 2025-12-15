import math
from typing import List

class CombinationCalculator: 
    def __init__(self, datas: List[str]):
        """
        Initialize the calculator with a list of data.
        """
        self.datas = datas

    def count(self, n: int, m: int) -> int:
        """
        Calculate the number of combinations for a specific count.
        :param n: The total number of elements,int.
        :param m: The number of elements in each combination,int.
        :return: The number of combinations,int.
        >>> CombinationCalculator.count(4, 2)
        6
        """
        if m == 0 or n == m:
            return 1
        return math.factorial(n) // (math.factorial(n - m) * math.factorial(m))
    
    @staticmethod
    def count_all(n: int) -> int:
        """
            Calculate the number of all possible combinations.
            :param n: The total number of elements,int.
            :return: The number of all possible combinations,int,if the number of combinations is greater than 2^63-1,return float("inf").
            >>> CombinationCalculator.count_all(4)
            15
            """
        if n < 0 or n > 63:
            return False
        return (1 << n) - 1 if n != 63 else float("inf")
    
    def select(self, m: int) -> List[List[str]]:
        """
        Generate combinations with a specified number of elements.
        :param m: The number of elements in each combination,int.
        :return: A list of combinations,List[List[str]].
        >>> calc = CombinationCalculator(["A", "B", "C", "D"])
        >>> calc.select(2)
        [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['B', 'D'], ['C', 'D']]
        """
        result = []
        self._select(0, [None] * m, 0, result)
        return result
    
    def _select(self, dataIndex: int, resultList: List[str], resultIndex: int, result: List[List[str]]):
        """
        Generate combinations with a specified number of elements by recursion.
        :param dataIndex: The index of the data to be selected,int.
        :param resultList: The list of elements in the combination,List[str].
        :param resultIndex: The index of the element in the combination,int.
        :param result: The list of combinations,List[List[str]].
        :return: None.
        >>> calc = CombinationCalculator(["A", "B", "C", "D"])
        >>> result = []
        >>> calc._select(0, [None] * 2, 0, result)
        >>> result
        [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['B', 'D'], ['C', 'D']]
        """
        resultLen = len(resultList)
        resultCount = resultIndex + 1
        if resultCount > resultLen:
            result.append(resultList.copy())
            return
    
        for i in range(dataIndex, len(self.datas) + resultCount - resultLen):
            resultList[resultIndex] = self.datas[i]
            self._select(i + 1, resultList, resultIndex + 1, result)

    def select_all(self) -> List[List[str]]:
        """
        दिए गए डेटा सूची से तत्वों का चयन करने के सभी संभावित संयोजनों को उत्पन्न करें, और यह चयन विधि का उपयोग करता है।
        :return: संयोजनों की एक सूची, List[List[str]]।
        >>> calc = CombinationCalculator(["A", "B", "C", "D"])
        >>> calc.select_all()
        [['A'], ['B'], ['C'], ['D'], ['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['B', 'D'], ['C', 'D'], ['A', 'B', 'C'], ['A', 'B', 'D'], ['A', 'C', 'D'], ['B', 'C', 'D'], ['A', 'B', 'C', 'D']]
        """
        result = []
        n = len(self.datas)
        for m in range(1, n + 1):
            self._select(0, [None] * m, 0, result)
        return result