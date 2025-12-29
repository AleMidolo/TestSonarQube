def answer(self, expression):
    """
        दिए गए गणितीय अभिव्यक्ति की जांच करें जो कार्ड का उपयोग करके 24 तक पहुंच सकती है।
        :param expression: स्ट्रिंग, कार्ड का उपयोग करके गणितीय अभिव्यक्ति
        :return: बूल, यदि अभिव्यक्ति 24 तक पहुंचती है तो True, अन्यथा False
        >>> game = TwentyFourPointGame()
        >>> game.nums = [4, 3, 6, 6]
        >>> ans = "4*3+6+6"
        >>> ret = game.answer(ans)
        True
        """
    if not self.evaluate_expression(expression):
        return False
    import re
    numbers_in_expr = re.findall('\\d+\\.?\\d*', expression)
    numbers_in_expr = [float(num) for num in numbers_in_expr]
    if len(numbers_in_expr) != 4:
        return False
    numbers_in_expr_sorted = sorted(numbers_in_expr)
    nums_sorted = sorted(self.nums)
    return numbers_in_expr_sorted == nums_sorted