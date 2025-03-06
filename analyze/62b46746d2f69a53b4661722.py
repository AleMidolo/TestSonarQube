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
    new_args = []
    for expr in args:
        if isinstance(expr, tuple):
            if expr[0] == '&':
                A, B = expr[1], expr[2]
                if isinstance(B, tuple) and B[0] == '|':
                    if B[1] == A:
                        # A & (A | B) = A
                        new_args.append(A)
                    elif B[1] == ('~', A):
                        # A & (~A | B) = A & B
                        new_args.append(('&', A, B[2]))
                    else:
                        new_args.append(expr)
                else:
                    new_args.append(expr)
            elif expr[0] == '|':
                A, B = expr[1], expr[2]
                if isinstance(B, tuple) and B[0] == '&':
                    if B[1] == A:
                        # A | (A & B) = A
                        new_args.append(A)
                    elif B[1] == ('~', A):
                        # A | (~A & B) = A | B
                        new_args.append(('|', A, B[2]))
                    else:
                        new_args.append(expr)
                else:
                    new_args.append(expr)
            else:
                new_args.append(expr)
        else:
            new_args.append(expr)
    return new_args