@staticmethod
def transform(expression):
    """
        इनफिक्स अभिव्यक्ति को रूपांतरित करने के लिए उपयुक्त प्रारूप में बदलें
        :param expression: स्ट्रिंग, रूपांतरित की जाने वाली इनफिक्स अभिव्यक्ति
        :return: स्ट्रिंग, रूपांतरित अभिव्यक्ति
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.transform("2 + 3 * 4")
        "2+3*4"
        """
    return re.sub('\\s+', '', expression)