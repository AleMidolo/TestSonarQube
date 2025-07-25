def absorb(self, args):
    """
    对于给定的表达式序列 `args`，返回一个应用吸收律的新表达式列表。

    对于给定的表达式序列 `args`，返回一个应用吸收律和负吸收律的新表达式列表。

    参考：https://en.wikipedia.org/wiki/Absorption_law

    吸收律（Absorption）::

      A & (A | B) = A, A | (A & B) = A

    负吸收律（Negative Absorption）::

      A & (~A | B) = A & B, A | (~A & B) = A | B
    """
    new_expressions = []
    for expr in args:
        # Apply Absorption Law
        if isinstance(expr, tuple) and len(expr) == 3:
            a, op, b = expr
            if op == '&':
                if (a == b) or (b == ('|', a)):
                    new_expressions.append(a)
                elif (a == ('|', b)):
                    new_expressions.append(a)
                elif (a == ('~', b)):
                    new_expressions.append(('&', a, b))
                else:
                    new_expressions.append(expr)
            elif op == '|':
                if (a == b) or (b == ('&', a)):
                    new_expressions.append(a)
                elif (a == ('~', b)):
                    new_expressions.append(('|', a, b))
                else:
                    new_expressions.append(expr)
        else:
            new_expressions.append(expr)
    return new_expressions