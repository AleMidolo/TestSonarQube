def select_all(self) -> List[List[str]]:
    """
        दिए गए डेटा सूची से तत्वों का चयन करने के सभी संभावित संयोजनों को उत्पन्न करें, और यह चयन विधि का उपयोग करता है।
        :return: संयोजनों की एक सूची, List[List[str]]।
        >>> calc = CombinationCalculator(["A", "B", "C", "D"])
        >>> calc.select_all()
        [['A'], ['B'], ['C'], ['D'], ['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['B', 'D'], ['C', 'D'], ['A', 'B', 'C'], ['A', 'B', 'D'], ['A', 'C', 'D'], ['B', 'C', 'D'], ['A', 'B', 'C', 'D']]
        """
    result = []
    n = len(self.datas)
    for m in range(1, n + 1):
        self._select(0, [None] * m, 0, result)
    return result