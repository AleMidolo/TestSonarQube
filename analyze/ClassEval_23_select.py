from typing import List

def select(self, m: int) -> List[List[str]]:
    """
    生成指定元素数量的组合。
    :param m: 每个组合中的元素数量，int。
    :return: 组合的列表，List[List[str]]。
    >>> calc = CombinationCalculator(["A", "B", "C", "D"])
    >>> calc.select(2)
    [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['B', 'D'], ['C', 'D']]

    """
    result = []
    n = len(self.elements)
    
    def backtrack(start: int, current: List[str]):
        # 如果当前组合已经有m个元素，添加到结果中
        if len(current) == m:
            result.append(current[:])
            return
        
        # 从start开始遍历，避免重复组合
        for i in range(start, n):
            current.append(self.elements[i])
            backtrack(i + 1, current)
            current.pop()
    
    backtrack(0, [])
    return result