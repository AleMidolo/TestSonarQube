def render(pieces, style):
    """
    Renderizzare i pezzi forniti nella versione richiesta dello stile.
    """
    if style == "bold":
        return [f"**{piece}**" for piece in pieces]
    elif style == "italic":
        return [f"*{piece}*" for piece in pieces]
    elif style == "underline":
        return [f"__{piece}__" for piece in pieces]
    else:
        return pieces