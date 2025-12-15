def compare(self, cur, peek):
        """
        दो ऑपरेटरों की प्राथमिकता की तुलना करें
        :param cur: स्ट्रिंग, वर्तमान ऑपरेटर
        :param peek: स्ट्रिंग, ऑपरेटर स्टैक के शीर्ष पर मौजूद ऑपरेटर
        :return: बूल, यदि वर्तमान ऑपरेटर की प्राथमिकता उच्च या समान है, तो True, अन्यथा False
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.compare("+", "-")
        True

        """
        return self.operat_priority[self.get_operator_index(cur)] >= self.operat_priority[self.get_operator_index(peek)]

    def get_operator_index(self, operator):
        """
        ऑपरेटर के लिए प्राथमिकता सूची में इंडेक्स प्राप्त करें
        :param operator: स्ट्रिंग, ऑपरेटर
        :return: int, ऑपरेटर का इंडेक्स
        """
        operators = {'+': 0, '-': 1, '*': 2, '\/': 3, '%': 4, '(': 5, ')': 6}
        return operators.get(operator, -1)