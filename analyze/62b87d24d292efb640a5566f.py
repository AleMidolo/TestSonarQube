def render(pieces, style):
    """
    Renderizzare i pezzi forniti nella versione richiesta dello stile.
    """
    if style == "plain":
        return "\n".join(pieces)
    elif style == "html":
        return "<ul>\n" + "\n".join(f"<li>{piece}</li>" for piece in pieces) + "\n</ul>"
    elif style == "markdown":
        return "\n".join(f"- {piece}" for piece in pieces)
    else:
        raise ValueError(f"Stile non supportato: {style}")