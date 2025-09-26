import itertools


class ArrangementCalculator:
    def __init__(self, datas):
        self.datas = datas

    @staticmethod
    def count(n, m=None):
        if m is None or n == m:
            return ArrangementCalculator.factorial(n)
        else:
            return ArrangementCalculator.factorial(n) // ArrangementCalculator.factorial(n - m)

    @staticmethod
    def count_all(n):
        return sum(ArrangementCalculator.count(n, i) for i in range(1, n + 1))

    def select(self, m=None):
        m = m if m is not None else len(self.datas)
        return [list(permutation) for permutation in itertools.permutations(self.datas, m)]

    def select_all(self):
        return [permutation for i in range(1, len(self.datas) + 1) for permutation in self.select(i)]

    @staticmethod
    def factorial(n):
        return 1 if n == 0 else n * ArrangementCalculator.factorial(n - 1)