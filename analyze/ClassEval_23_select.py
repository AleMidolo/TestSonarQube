def select(self, m: int) -> List[List[str]]:
    """
    Genera combinazioni con un numero specificato di elementi.
    :param m: Il numero di elementi in ogni combinazione, int.
    :return: Una lista di combinazioni, List[List[str]].
    >>> calc = CombinationCalculator(["A", "B", "C", "D"])
    >>> calc.select(2)
    [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['B', 'D'], ['C', 'D']]

    """
    if m < 0 or m > len(self.data):
        return []
    
    if m == 0:
        return [[]]
    
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