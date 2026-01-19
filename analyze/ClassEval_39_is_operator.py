@staticmethod
def is_operator(c):
    """
        जांचें कि क्या एक वर्ण {'+', '-', '*', '/', '(', ')', '%'} में एक ऑपरेटर है
        :param c: स्ट्रिंग, जांचने के लिए वर्ण
        :return: बूल, यदि वर्ण एक ऑपरेटर है तो True, अन्यथा False
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.is_operator("+")
        True

        """
    return c in {'+', '-', '*', '\\/', '(', ')', '%'}