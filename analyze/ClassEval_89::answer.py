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
    import re
    numbers_in_expression = re.findall('\\d+', expression)
    numbers_in_expression = [int(num) for num in numbers_in_expression]
    nums_sorted = sorted(self.nums)
    expr_sorted = sorted(numbers_in_expression)
    if nums_sorted != expr_sorted:
        return False
    return self.evaluate_expression(expression)