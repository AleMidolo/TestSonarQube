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
                left, right = expr[1], expr[2]
                if isinstance(right, tuple) and right[0] == '|':
                    if left == right[1]:
                        return left
                    elif left == ('~', right[1]):
                        return ('&', left, right[2])
                elif isinstance(left, tuple) and left[0] == '|':
                    if right == left[1]:
                        return right
                    elif right == ('~', left[1]):
                        return ('&', right, left[2])
            elif expr[0] == '|':
                left, right = expr[1], expr[2]
                if isinstance(right, tuple) and right[0] == '&':
                    if left == right[1]:
                        return left
                    elif left == ('~', right[1]):
                        return ('|', left, right[2])
                elif isinstance(left, tuple) and left[0] == '&':
                    if right == left[1]:
                        return right
                    elif right == ('~', left[1]):
                        return ('|', right, left[2])
        return expr

    return [apply_absorption(arg) for arg in args]