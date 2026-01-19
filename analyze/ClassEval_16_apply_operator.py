def apply_operator(self, operand_stack, operator_stack):
    """
    使用操作符栈顶部的操作符对操作数栈顶部的两个数字执行操作，并将结果存储在操作数栈顶部
    :param operand_stack:list
    :param operator_stack:list
    :return: 更新后的 operand_stack 和 operator_stack
    >>> calculator = Calculator()
    >>> calculator.apply_operator([1, 2, 3], ['+', '-'])
    ([1, -1], ['-'])
    """
    if len(operand_stack) < 2 or len(operator_stack) == 0:
        return operand_stack, operator_stack
    
    # 从操作符栈弹出操作符
    operator = operator_stack.pop()
    
    # 从操作数栈弹出两个操作数（注意顺序：后弹出的是左操作数）
    right_operand = operand_stack.pop()
    left_operand = operand_stack.pop()
    
    # 根据操作符执行相应的运算
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
    else:
        result = 0
    
    # 将结果压入操作数栈
    operand_stack.append(result)
    
    return operand_stack, operator_stack