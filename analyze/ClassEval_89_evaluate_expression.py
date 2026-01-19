def evaluate_expression(self, expression):
    """
    एक गणितीय अभिव्यक्ति का मूल्यांकन करें और जांचें कि क्या परिणाम 24 है।
    :param expression: स्ट्रिंग, गणितीय अभिव्यक्ति
    :return: बूल, यदि अभिव्यक्ति 24 के बराबर है तो True, अन्यथा False
    >>> game = TwentyFourPointGame()
    >>> nums = [4, 3, 6, 6]
    >>> ans = "4*3+6+6"
    >>> ret = game.evaluate_expression(ans)
    True
    """
    try:
        # Evaluate the mathematical expression
        result = eval(expression)
        
        # Check if the result equals 24 (with floating point tolerance)
        return abs(result - 24) < 1e-6
    except:
        # If there's any error in evaluation, return False
        return False