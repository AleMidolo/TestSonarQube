def evaluate_expression(self, expression):
    """
        एक गणितीय अभिव्यक्ति का मूल्यांकन करें और जांचें कि क्या परिणाम 24 है।
        :param expression: स्ट्रिंग, गणितीय अभिव्यक्ति
        :return: बूल, यदि अभिव्यक्ति 24 के बराबर है तो True, अन्यथा False
        >>> game = TwentyFourPointGame()
        >>> nums = [4, 3, 6, 6]
        >>> ans = "4*3+6+6"
        >>> ret = game.evaluate_expression(ans)
        True
        """
    try:

        class SafeEvaluator(ast.NodeVisitor):

            def __init__(self):
                self.allowed_nodes = {ast.Expression, ast.BinOp, ast.UnaryOp, ast.Constant, ast.Add, ast.Sub, ast.Mult, ast.Div, ast.USub, ast.UAdd}

            def visit(self, node):
                if type(node) not in self.allowed_nodes:
                    raise ValueError(f'Disallowed node type: {type(node).__name__}')
                return super().visit(node)
        tree = ast.parse(expression, mode='eval')
        validator = SafeEvaluator()
        validator.visit(tree)
        result = eval(compile(tree, '<string>', 'eval'))
        return abs(result - 24) < 1e-10
    except (SyntaxError, ValueError, ZeroDivisionError, TypeError):
        return False