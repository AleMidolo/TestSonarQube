def render(pieces, style):
    """
    Renderizzare i pezzi forniti nella versione richiesta dello stile.
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
            rendered_output.append(piece)
    return ''.join(rendered_output)