def render(pieces, style):
    """
    Renderiza las piezas de versión dadas en el estilo solicitado.
    """
    rendered = []
    
    for piece in pieces:
        if style == "dots":
            rendered.append(piece.replace(".", "•"))
        elif style == "arrows":
            rendered.append(piece.replace("<", "←").replace(">", "→"))
        elif style == "unicode":
            rendered.append(piece.replace("-", "─").replace("|", "│"))
        else:
            rendered.append(piece)
            
    return rendered