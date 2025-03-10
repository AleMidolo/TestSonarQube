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
                a, b = expr[1], expr[2]
                if isinstance(b, tuple) and b[0] == '|':
                    if a == b[1]:
                        new_args.append(a)
                    elif a == ('~', b[1]):
                        new_args.append(('&', a, b[2]))
                    else:
                        new_args.append(expr)
                else:
                    new_args.append(expr)
            elif expr[0] == '|':
                a, b = expr[1], expr[2]
                if isinstance(b, tuple) and b[0] == '&':
                    if a == b[1]:
                        new_args.append(a)
                    elif a == ('~', b[1]):
                        new_args.append(('|', a, b[2]))
                    else:
                        new_args.append(expr)
                else:
                    new_args.append(expr)
            else:
                new_args.append(expr)
        else:
            new_args.append(expr)
    return new_args