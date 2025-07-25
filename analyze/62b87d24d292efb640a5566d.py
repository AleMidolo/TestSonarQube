def plus_or_dot(pieces):
    """
     यदि हमारे पास पहले से "+" है, तो "." लौटाएं, अन्यथा "+" लौटाएं।
    """
    if '+' in pieces:
        return '.'
    else:
        return '+'