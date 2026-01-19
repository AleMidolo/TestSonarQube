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
    
    try:
        # Extract all numbers from the expression
        numbers_in_expr = re.findall(r'\d+', expression)
        numbers_in_expr = [int(n) for n in numbers_in_expr]
        
        # Sort both lists to compare
        sorted_nums = sorted(self.nums)
        sorted_expr_nums = sorted(numbers_in_expr)
        
        # Check if the numbers used in expression match the available numbers
        if sorted_nums != sorted_expr_nums:
            return False
        
        # Evaluate the expression
        result = eval(expression)
        
        # Check if result equals 24 (with small tolerance for floating point)
        if abs(result - 24) < 1e-6:
            return True
        else:
            return False
            
    except:
        return False