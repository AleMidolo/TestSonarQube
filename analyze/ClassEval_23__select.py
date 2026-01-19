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
    # 如果已经选择了足够的元素（resultIndex达到resultList的长度）
    if resultIndex == len(resultList):
        # 将当前组合添加到结果列表中
        result.append(resultList[:])
        return
    
    # 如果数据索引超出范围，返回
    if dataIndex >= len(self.data):
        return
    
    # 计算还需要选择的元素数量
    remaining = len(resultList) - resultIndex
    # 计算剩余可用的元素数量
    available = len(self.data) - dataIndex
    
    # 如果剩余可用元素不足，返回
    if available < remaining:
        return
    
    # 选择当前元素
    resultList[resultIndex] = self.data[dataIndex]
    self._select(dataIndex + 1, resultList, resultIndex + 1, result)
    
    # 不选择当前元素，继续下一个
    self._select(dataIndex + 1, resultList, resultIndex, result)