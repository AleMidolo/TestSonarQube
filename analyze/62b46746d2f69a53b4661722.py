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
        # Apply absorption laws
        if '&' in expr and '|' in expr:
            # Check for A & (A | B)
            if expr.count('&') == 1 and expr.count('|') == 1:
                parts = expr.split('&')
                A = parts[0].strip()
                B = parts[1].strip().split('|')[1].strip() if '|' in parts[1] else ''
                if A in parts[1]:
                    result.append(A)
                    continue
            # Check for A | (A & B)
            if expr.count('|') == 1 and expr.count('&') == 1:
                parts = expr.split('|')
                A = parts[0].strip()
                B = parts[1].strip().split('&')[1].strip() if '&' in parts[1] else ''
                if A in parts[1]:
                    result.append(A)
                    continue
        
        # Apply negative absorption laws
        if '&' in expr and '~' in expr:
            # Check for A & (~A | B)
            if expr.count('&') == 1 and expr.count('|') == 1:
                parts = expr.split('&')
                A = parts[0].strip()
                neg_part = parts[1].strip()
                if '~' in neg_part:
                    B = neg_part.split('|')[1].strip() if '|' in neg_part else ''
                    result.append(f"{A} & {B}")
                    continue
            # Check for A | (~A & B)
            if expr.count('|') == 1 and expr.count('&') == 1:
                parts = expr.split('|')
                A = parts[0].strip()
                neg_part = parts[1].strip()
                if '~' in neg_part:
                    B = neg_part.split('&')[1].strip() if '&' in neg_part else ''
                    result.append(f"{A} | {B}")
                    continue
        
        # If no absorption or negative absorption applied, keep the original expression
        result.append(expr)
    
    return result