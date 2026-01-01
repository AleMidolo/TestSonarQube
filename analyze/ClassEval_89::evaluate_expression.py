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
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        tokens = []
        i = 0
        while i < len(expression):
            if expression[i].isdigit():
                j = i
                while j < len(expression) and expression[j].isdigit():
                    j += 1
                tokens.append(int(expression[i:j]))
                i = j
            else:
                if expression[i] in '+-*/':
                    tokens.append(expression[i])
                i += 1
        output = []
        operators = []
        for token in tokens:
            if isinstance(token, int):
                output.append(token)
            elif token in '+-*/':
                while operators and operators[-1] in '+-*/' and (precedence[operators[-1]] >= precedence[token]):
                    output.append(operators.pop())
                operators.append(token)
        while operators:
            output.append(operators.pop())
        stack = []
        ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        for token in output:
            if isinstance(token, int):
                stack.append(float(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == '/' and b == 0:
                    return False
                stack.append(ops[token](a, b))
        result = stack[0]
        return abs(result - 24) < 1e-10
    except Exception:
        return False