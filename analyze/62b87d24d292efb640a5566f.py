def render(pieces, style):
    """
    Renderiza las piezas de versión dadas en el estilo solicitado.
    """
    rendered_output = []
    for piece in pieces:
        if style == 'bold':
            rendered_output.append(f"**{piece}**")
        elif style == 'italic':
            rendered_output.append(f"*{piece}*")
        elif style == 'underline':
            rendered_output.append(f"__{piece}__")
        else:
            rendered_output.append(piece)  # Default to plain text
    return '\n'.join(rendered_output)