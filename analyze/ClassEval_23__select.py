def _select(self, dataIndex: int, resultList: List[str], resultIndex: int, result: List[List[str]]):
    """
    पुनरावृत्ति द्वारा निर्दिष्ट संख्या के तत्वों के साथ संयोजन उत्पन्न करें।
    :param dataIndex: चयनित डेटा का अनुक्रमांक, int.
    :param resultList: संयोजन में तत्वों की सूची, List[str].
    :param resultIndex: संयोजन में तत्व का अनुक्रमांक, int.
    :param result: संयोजनों की सूची, List[List[str]].
    :return: कुछ नहीं।
    >>> calc = CombinationCalculator(["A", "B", "C", "D"])
    >>> result = []
    >>> calc._select(0, [None] * 2, 0, result)
    >>> result
    [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['B', 'D'], ['C', 'D']]

    """
    # Base case: if we've filled all positions in resultList, add it to result
    if resultIndex == len(resultList):
        result.append(resultList[:])
        return
    
    # Recursive case: try each element from dataIndex onwards
    for i in range(dataIndex, len(self.data)):
        # Place current element at resultIndex position
        resultList[resultIndex] = self.data[i]
        # Recursively fill the next position, starting from i+1 to avoid duplicates
        self._select(i + 1, resultList, resultIndex + 1, result)