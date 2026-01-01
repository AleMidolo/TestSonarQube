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
    try:
        node = ast.parse(expression, mode='eval')
        allowed_operators = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul, ast.Div: operator.truediv, ast.Pow: operator.pow, ast.USub: operator.neg, ast.UAdd: operator.pos}

        def eval_node(node):
            if isinstance(node, ast.Num):
                return node.n
            elif isinstance(node, ast.UnaryOp):
                return allowed_operators[type(node.op)](eval_node(node.operand))
            elif isinstance(node, ast.BinOp):
                left_val = eval_node(node.left)
                right_val = eval_node(node.right)
                op_type = type(node.op)
                if op_type not in allowed_operators:
                    raise ValueError(f'Operator {op_type} not allowed')
                if op_type == ast.Div and right_val == 0:
                    raise ZeroDivisionError('Division by zero')
                return allowed_operators[op_type](left_val, right_val)
            elif isinstance(node, ast.Constant):
                return node.value
            else:
                raise ValueError(f'Unsupported AST node: {type(node)}')
        result = eval_node(node.body)
        return abs(result - 24) < 1e-10
    except (SyntaxError, ValueError, ZeroDivisionError, TypeError, AttributeError):
        return False