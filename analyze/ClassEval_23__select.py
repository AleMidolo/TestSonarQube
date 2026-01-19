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
    # 获取组合的大小
    n = len(resultList)
    
    # 如果已经选择了足够的元素，将当前组合添加到结果中
    if resultIndex == n:
        result.append(resultList[:])
        return
    
    # 计算还需要选择多少个元素
    remaining = n - resultIndex
    
    # 从dataIndex开始遍历数据
    # 确保剩余的数据足够完成组合
    for i in range(dataIndex, len(self.data) - remaining + 1):
        resultList[resultIndex] = self.data[i]
        self._select(i + 1, resultList, resultIndex + 1, result)