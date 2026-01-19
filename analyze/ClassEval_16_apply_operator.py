def apply_operator(self, operand_stack, operator_stack):
    """
        ऑपरेटर स्टैक के शीर्ष पर मौजूद ऑपरेटर का उपयोग करके ऑपरेशन को ऑपरेटर स्टैक के शीर्ष पर मौजूद दो संख्याओं पर लागू करें, और परिणामों को ऑपरेटर स्टैक के शीर्ष पर स्टोर करें
        :param operand_stack:list
        :param operator_stack:list
        :return: अपडेटेड operand_stack और operator_stack
        >>> calculator = Calculator()
        >>> calculator.apply_operator([1, 2, 3], ['+', '-'])
        ([1, -1], ['-'])
        """
    if len(operand_stack) < 2 or not operator_stack:
        return (operand_stack, operator_stack)
    operator = operator_stack.pop()
    b = operand_stack.pop()
    a = operand_stack.pop()
    try:
        result = self.operators[operator](a, b)
        operand_stack.append(result)
    except (ZeroDivisionError, KeyError):
        return (operand_stack, operator_stack)
    return (operand_stack, operator_stack)