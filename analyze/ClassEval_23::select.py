def select(self, m: int) -> List[List[str]]:
    """
        निर्दिष्ट संख्या के तत्वों के साथ संयोजन उत्पन्न करें।
        :param m: प्रत्येक संयोजन में तत्वों की संख्या, int.
        :return: संयोजनों की एक सूची, List[List[str]].
        >>> calc = CombinationCalculator(["A", "B", "C", "D"])
        >>> calc.select(2)
        [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['B', 'D'], ['C', 'D']]

        """
    if m <= 0 or m > len(self.datas):
        return []
    result = []
    resultList = [None] * m
    self._select(0, resultList, 0, result)
    return result