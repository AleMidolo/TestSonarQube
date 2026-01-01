def _select(self, dataIndex: int, resultList: List[str], resultIndex: int, result: List[List[str]]):
    """
        通过递归生成具有指定元素数量的组合。
        :param dataIndex: 要选择的数据的索引，int。
        :param resultList: 组合中元素的列表，List[str]。
        :param resultIndex: 组合中元素的索引，int。
        :param result: 组合的列表，List[List[str]]。
        :return: None。
        >>> calc = CombinationCalculator(["A", "B", "C", "D"])
        >>> result = []
        >>> calc._select(0, [None] * 2, 0, result)
        >>> result
        [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['B', 'D'], ['C', 'D']]
        """
    if resultIndex == len(resultList):
        result.append(resultList.copy())
        return
    if dataIndex >= len(self.datas):
        return
    resultList[resultIndex] = self.datas[dataIndex]
    self._select(dataIndex + 1, resultList, resultIndex + 1, result)
    self._select(dataIndex + 1, resultList, resultIndex, result)