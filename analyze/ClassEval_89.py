import random


class TwentyFourPointGame:
    MAX_CARDS = 4
    TARGET_VALUE = 24
    MIN_CARD_VALUE = 1
    MAX_CARD_VALUE = 9

    def __init__(self) -> None:
        self.nums = []

    def _generate_cards(self):
        self.nums = [random.randint(self.MIN_CARD_VALUE, self.MAX_CARD_VALUE) for _ in range(self.MAX_CARDS)]
        assert len(self.nums) == self.MAX_CARDS

    def get_my_cards(self):
        self._generate_cards()
        return self.nums

    def answer(self, expression):
        if expression == 'pass':
            return self.get_my_cards()
        
        statistic = self._count_used_numbers(expression)

        if not self._are_numbers_available(statistic):
            return False

        if all(count == 0 for count in statistic.values()):
            return self.evaluate_expression(expression)
        else:
            return False

    def _count_used_numbers(self, expression):
        statistic = {}
        for c in expression:
            if c.isdigit() and int(c) in self.nums:
                statistic[c] = statistic.get(c, 0) + 1
        return statistic

    def _are_numbers_available(self, statistic):
        nums_used = statistic.copy()
        for num in self.nums:
            if nums_used.get(str(num), -1) > 0:
                nums_used[str(num)] -= 1
            else:
                return False
        return True

    def evaluate_expression(self, expression):
        try:
            return eval(expression) == self.TARGET_VALUE
        except Exception:
            return False