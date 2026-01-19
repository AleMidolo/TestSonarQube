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
    if resultIndex == len(resultList):
        result.append(resultList.copy())
        return
    for i in range(dataIndex, len(self.datas)):
        resultList[resultIndex] = self.datas[i]
        self._select(i + 1, resultList, resultIndex + 1, result)