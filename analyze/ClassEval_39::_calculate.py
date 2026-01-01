@staticmethod
def _calculate(first_value, second_value, current_op):
    """
        根据给定的操作数和运算符执行数学计算
        :param first_value: 字符串, 第一个操作数
        :param second_value: 字符串, 第二个操作数
        :param current_op: 字符串, 运算符
        :return: decimal.Decimal, 计算结果
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator._calculate("2", "3", "+")
        5.0
        """
    first = Decimal(first_value)
    second = Decimal(second_value)
    if current_op == '+':
        result = first + second
    elif current_op == '-':
        result = first - second
    elif current_op == '*':
        result = first * second
    elif current_op == '/':
        if second == 0:
            raise ZeroDivisionError('Division by zero')
        result = first / second
    elif current_op == '%':
        if second == 0:
            raise ZeroDivisionError('Modulo by zero')
        result = first % second
    else:
        raise ValueError(f'Unsupported operator: {current_op}')
    return result