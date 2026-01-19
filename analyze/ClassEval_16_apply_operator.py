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
    # Pop the operator from operator_stack
    operator = operator_stack.pop()
    
    # Pop two operands from operand_stack (right operand first, then left)
    right_operand = operand_stack.pop()
    left_operand = operand_stack.pop()
    
    # Apply the operator
    if operator == '+':
        result = left_operand + right_operand
    elif operator == '-':
        result = left_operand - right_operand
    elif operator == '*':
        result = left_operand * right_operand
    elif operator == '/':
        result = left_operand / right_operand
    elif operator == '//':
        result = left_operand // right_operand
    elif operator == '%':
        result = left_operand % right_operand
    elif operator == '**':
        result = left_operand ** right_operand
    
    # Push the result back to operand_stack
    operand_stack.append(result)
    
    return operand_stack, operator_stack