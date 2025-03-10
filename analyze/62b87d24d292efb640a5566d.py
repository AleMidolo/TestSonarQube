def plus_or_dot(pieces):
    """
    如果片段的闭合标签（closet-tag）中包含 "+"，则返回 "."；否则，返回 "+"。
    如果尚未存在“+”，则返回“+”，否则返回“.”。
    """
    for piece in pieces:
        if '+' in piece:
            return '.'
    return '+'