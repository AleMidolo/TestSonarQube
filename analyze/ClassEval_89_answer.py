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
    try:
        # Extract numbers from the expression
        import re
        numbers_in_expr = []
        for char in expression:
            if char.isdigit():
                numbers_in_expr.append(int(char))
        
        # Sort both lists to compare
        numbers_in_expr_sorted = sorted(numbers_in_expr)
        nums_sorted = sorted(self.nums)
        
        # Check if the numbers used match the available numbers
        if numbers_in_expr_sorted != nums_sorted:
            return False
        
        # Evaluate the expression
        result = eval(expression)
        
        # Check if result equals 24
        return abs(result - 24) < 1e-6
    
    except:
        return False