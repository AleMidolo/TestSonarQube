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
        safe_operators = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul, ast.Div: operator.truediv, ast.Pow: operator.pow, ast.USub: operator.neg, ast.UAdd: operator.pos}

        def eval_node(node):
            if isinstance(node, ast.Num):
                return node.n
            elif isinstance(node, ast.BinOp):
                left = eval_node(node.left)
                right = eval_node(node.right)
                op_type = type(node.op)
                if op_type in safe_operators:
                    if op_type == ast.Div and abs(right) < 1e-10:
                        raise ZeroDivisionError
                    return safe_operators[op_type](left, right)
                else:
                    raise ValueError(f'Unsupported operator: {op_type}')
            elif isinstance(node, ast.UnaryOp):
                operand = eval_node(node.operand)
                op_type = type(node.op)
                if op_type in safe_operators:
                    return safe_operators[op_type](operand)
                else:
                    raise ValueError(f'Unsupported operator: {op_type}')
            else:
                raise ValueError(f'Unsupported node type: {type(node)}')
        result = eval_node(node.body)
        return result
    except:
        try:
            allowed_names = {'__builtins__': None}
            result = eval(expression, allowed_names, {})
            return result
        except:
            raise ValueError('Invalid expression')