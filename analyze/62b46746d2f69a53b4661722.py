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
                A, B = expr[1], expr[2]
                if isinstance(B, tuple) and B[0] == '|' and B[1] == A:
                    return A
                if isinstance(B, tuple) and B[0] == '|' and isinstance(B[1], tuple) and B[1][0] == '~' and B[1][1] == A:
                    return ('&', A, B[2])
            elif expr[0] == '|':
                A, B = expr[1], expr[2]
                if isinstance(B, tuple) and B[0] == '&' and B[1] == A:
                    return A
                if isinstance(B, tuple) and B[0] == '&' and isinstance(B[1], tuple) and B[1][0] == '~' and B[1][1] == A:
                    return ('|', A, B[2])
        return expr

    return [apply_absorption(arg) for arg in args]