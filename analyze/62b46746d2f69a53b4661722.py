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
    def apply_absorption(expr):
        if isinstance(expr, tuple):
            if expr[0] == '&':
                a, b = expr[1], expr[2]
                if isinstance(b, tuple) and b[0] == '|':
                    if a == b[1]:
                        return a
                    elif a == ('~', b[1]):
                        return ('&', a, b[2])
                elif isinstance(b, tuple) and b[0] == '&':
                    if a == b[1]:
                        return a
            elif expr[0] == '|':
                a, b = expr[1], expr[2]
                if isinstance(b, tuple) and b[0] == '&':
                    if a == b[1]:
                        return a
                    elif a == ('~', b[1]):
                        return ('|', a, b[2])
                elif isinstance(b, tuple) and b[0] == '|':
                    if a == b[1]:
                        return a
        return expr

    return [apply_absorption(arg) for arg in args]