def evaluate_expression(self, expression):
    """
        Evaluate a mathematical expression and check if the result is 24.
        :param expression: string, mathematical expression
        :return: bool, True if the expression equals 24, otherwise False
        >>> game = TwentyFourPointGame()
        >>> nums = [4, 3, 6, 6]
        >>> ans = "4*3+6+6"
        >>> ret = game.evaluate_expression(ans)
        True
        """
    try:
        node = ast.parse(expression, mode='eval')
        operators = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul, ast.Div: operator.truediv, ast.Pow: operator.pow, ast.USub: operator.neg, ast.UAdd: operator.pos}

        def eval_node(node):
            if isinstance(node, ast.Num):
                return float(node.n)
            elif isinstance(node, ast.BinOp):
                left = eval_node(node.left)
                right = eval_node(node.right)
                op = operators[type(node.op)]
                try:
                    return op(left, right)
                except ZeroDivisionError:
                    return float('inf')
            elif isinstance(node, ast.UnaryOp):
                operand = eval_node(node.operand)
                op = operators[type(node.op)]
                return op(operand)
            else:
                raise TypeError(f'Unsupported operation: {type(node)}')
        result = eval_node(node.body)
        return abs(result - 24) < 1e-10
    except Exception as e:
        return False