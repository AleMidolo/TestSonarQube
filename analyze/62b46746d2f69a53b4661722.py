def absorb(self, args):
    """
    `args` अभिव्यक्तियों के अनुक्रम को दिया गया है, एक नई सूची लौटाएं जिसमें अवशोषण और नकारात्मक अवशोषण लागू किया गया हो।

    अधिक जानकारी के लिए देखें: [https://en.wikipedia.org/wiki/Absorption_law](https://en.wikipedia.org/wiki/Absorption_law)

    **अवशोषण (Absorption):**

    A & (A | B) = A, A | (A & B) = A

    **नकारात्मक अवशोषण (Negative Absorption):**

    A & (~A | B) = A & B, A | (~A & B) = A | B
    """
    result = []
    for expr in args:
        if isinstance(expr, tuple):
            if len(expr) == 3:
                op, left, right = expr
                if op == '&':
                    if left == right:
                        result.append(left)
                    elif isinstance(right, tuple) and right[0] == '|' and right[1] == left:
                        result.append(left)
                    elif isinstance(right, tuple) and right[0] == '|' and right[1] == ('~', left):
                        result.append(('&', left, right[2]))
                elif op == '|':
                    if left == right:
                        result.append(left)
                    elif isinstance(right, tuple) and right[0] == '&' and right[1] == left:
                        result.append(left)
                    elif isinstance(right, tuple) and right[0] == '&' and right[1] == ('~', left):
                        result.append(('|', left, right[2]))
                else:
                    result.append(expr)
            else:
                result.append(expr)
        else:
            result.append(expr)
    return result