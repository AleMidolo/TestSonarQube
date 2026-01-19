def evaluate_expression(self, expression):
    """
        Valuta un'espressione matematica e verifica se il risultato è 24.
        :param expression: stringa, espressione matematica
        :return: bool, True se l'espressione si valuta a 24, False altrimenti
        >>> game = TwentyFourPointGame()
        >>> nums = [4, 3, 6, 6]
        >>> ans = "4*3+6+6"
        >>> ret = game.evaluate_expression(ans)
        True
        """
    safe_operators = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul, ast.Div: operator.truediv, ast.Pow: operator.pow, ast.USub: operator.neg, ast.UAdd: operator.pos}

    def safe_eval(node):
        if isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.BinOp):
            left = safe_eval(node.left)
            right = safe_eval(node.right)
            if node.op.__class__ in safe_operators:
                op_func = safe_operators[node.op.__class__]
                try:
                    return op_func(left, right)
                except ZeroDivisionError:
                    raise ValueError('Division by zero')
            else:
                raise ValueError(f'Unsupported operator: {node.op.__class__}')
        elif isinstance(node, ast.UnaryOp):
            operand = safe_eval(node.operand)
            if node.op.__class__ in safe_operators:
                op_func = safe_operators[node.op.__class__]
                return op_func(operand)
            else:
                raise ValueError(f'Unsupported unary operator: {node.op.__class__}')
        else:
            raise ValueError(f'Unsupported AST node: {node.__class__}')
    try:
        tree = ast.parse(expression, mode='eval')
        result = safe_eval(tree.body)
        return result
    except:
        raise ValueError('Invalid expression')