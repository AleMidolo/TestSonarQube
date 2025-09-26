import random


class TwentyFourPointGame:
    def __init__(self) -> None:
        self.nums = []

    def _generate_cards(self):
        self.nums = [random.randint(1, 9) for _ in range(4)]
        assert len(self.nums) == 4

    def get_my_cards(self):
        self._generate_cards()
        return self.nums

    def answer(self, expression):
        if expression == 'pass':
            return self.get_my_cards()
        
        statistic = self._count_used_numbers(expression)

        if not self._are_numbers_available(statistic):
            return False

        return self._evaluate_expression_if_all_used(statistic, expression)

    def _count_used_numbers(self, expression):
        statistic = {}
        for c in expression:
            if c.isdigit() and int(c) in self.nums:
                statistic[c] = statistic.get(c, 0) + 1
        return statistic

    def _are_numbers_available(self, nums_used):
        for num in self.nums:
            if nums_used.get(str(num), -100) != -100 and nums_used[str(num)] > 0:
                nums_used[str(num)] -= 1
            else:
                return False
        return True

    def _evaluate_expression_if_all_used(self, nums_used, expression):
        if all(count == 0 for count in nums_used.values()):
            return self.evaluate_expression(expression)
        return False

    def evaluate_expression(self, expression):
        try:
            return eval(expression) == 24
        except Exception:
            return False