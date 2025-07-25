def absorb(self, args):
    """
    Given an `args` sequence of expressions, return a new list of expression
    applying absorption and negative absorption.

    See https://en.wikipedia.org/wiki/Absorption_law

    Absorption::

        A & (A | B) = A, A | (A & B) = A

    Negative absorption::

        A & (~A | B) = A & B, A | (~A & B) = A | B
    """
    result = []
    for expr in args:
        if isinstance(expr, tuple) and len(expr) == 3:
            a, op, b = expr
            if op == '&':
                if (a == b) or (b == ('|', a)):
                    result.append(a)
                elif (a == ('~', b)) or (b == ('|', ('~', a))):
                    result.append(('&', a, b))
                else:
                    result.append(expr)
            elif op == '|':
                if (a == b) or (b == ('&', a)):
                    result.append(a)
                elif (a == ('~', b)) or (b == ('&', ('~', a))):
                    result.append(('|', a, b))
                else:
                    result.append(expr)
        else:
            result.append(expr)
    return result