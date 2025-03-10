def render(pieces, style):
    """
    Renderizzare i pezzi forniti nella versione richiesta dello stile.
    
    :param pieces: Lista di pezzi da renderizzare.
    :param style: Stile di renderizzazione richiesto.
    :return: Stringa rappresentante i pezzi renderizzati nello stile specificato.
    """
    if style == "plain":
        return "\n".join(pieces)
    elif style == "html":
        return "<ul>\n" + "\n".join(f"<li>{piece}</li>" for piece in pieces) + "\n</ul>"
    elif style == "json":
        import json
        return json.dumps(pieces)
    else:
        raise ValueError(f"Stile non supportato: {style}")