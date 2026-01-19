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
    if len(operand_stack) < 2 or len(operator_stack) < 1:
        return operand_stack, operator_stack
    
    # Pop the top operator
    operator = operator_stack.pop()
    
    # Pop two operands (top two elements)
    operand2 = operand_stack.pop()
    operand1 = operand_stack.pop()
    
    # Apply the operator
    if operator == '+':
        result = operand1 + operand2
    elif operator == '-':
        result = operand1 - operand2
    elif operator == '*':
        result = operand1 * operand2
    elif operator == '/':
        result = operand1 / operand2
    else:
        result = 0
    
    # Push the result back to operand_stack
    operand_stack.append(result)
    
    return operand_stack, operator_stack