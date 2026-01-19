def prepare(self, expression):
    """
    准备中缀表达式以便转换为后缀表示法
    :param expression: 字符串，要准备的中缀表达式
    >>> expression_calculator = ExpressionCalculator()
    >>> expression_calculator.prepare("2+3*4")

    expression_calculator.postfix_stack = ['2', '3', '4', '*', '+']
    """
    # 定义运算符优先级
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    
    # 初始化输出列表和运算符栈
    output = []
    operator_stack = []
    
    # 移除空格
    expression = expression.replace(' ', '')
    
    i = 0
    while i < len(expression):
        char = expression[i]
        
        # 如果是数字（包括多位数和小数）
        if char.isdigit() or char == '.':
            num = ''
            while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                num += expression[i]
                i += 1
            output.append(num)
            continue
        
        # 如果是左括号
        elif char == '(':
            operator_stack.append(char)
        
        # 如果是右括号
        elif char == ')':
            while operator_stack and operator_stack[-1] != '(':
                output.append(operator_stack.pop())
            if operator_stack:
                operator_stack.pop()  # 移除左括号
        
        # 如果是运算符
        elif char in precedence:
            while (operator_stack and 
                   operator_stack[-1] != '(' and
                   operator_stack[-1] in precedence and
                   precedence[operator_stack[-1]] >= precedence[char]):
                output.append(operator_stack.pop())
            operator_stack.append(char)
        
        i += 1
    
    # 将剩余的运算符弹出
    while operator_stack:
        output.append(operator_stack.pop())
    
    # 将结果存储到实例变量中
    self.postfix_stack = output