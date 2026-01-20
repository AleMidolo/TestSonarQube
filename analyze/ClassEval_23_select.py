from typing import List

def select(self, m: int) -> List[List[str]]:
    """
    Generar combinaciones con un número especificado de elementos.
    :param m: El número de elementos en cada combinación, int.
    :return: Una lista de combinaciones, List[List[str]].
    >>> calc = CombinationCalculator(["A", "B", "C", "D"])
    >>> calc.select(2)
    [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['B', 'D'], ['C', 'D']]

    """
    if m == 0:
        return [[]]
    if m > len(self.data):
        return []
    
    result = []
    
    def backtrack(start: int, current: List[str]):
        if len(current) == m:
            result.append(current[:])
            return
        
        for i in range(start, len(self.data)):
            current.append(self.data[i])
            backtrack(i + 1, current)
            current.pop()
    
    backtrack(0, [])
    return result