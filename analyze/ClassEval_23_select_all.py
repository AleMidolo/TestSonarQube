def select_all(self) -> List[List[str]]:
    """
        生成从给定数据列表中选择元素的所有可能组合，并使用select方法。
        :return: 组合的列表，List[List[str]]。
        >>> calc = CombinationCalculator(["A", "B", "C", "D"])
        >>> calc.select_all()
        [['A'], ['B'], ['C'], ['D'], ['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['B', 'D'], ['C', 'D'], ['A', 'B', 'C'], ['A', 'B', 'D'], ['A', 'C', 'D'], ['B', 'C', 'D'], ['A', 'B', 'C', 'D']]
        """
    result = []
    n = len(self.datas)
    for m in range(1, n + 1):
        result.extend(self.select(m))
    return result