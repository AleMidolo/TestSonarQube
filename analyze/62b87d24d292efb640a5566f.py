def render(pieces, style):
    """
    Renderizzare i pezzi forniti nella versione richiesta dello stile.
    """
    if style == "simple":
        return "\n".join(pieces)
    elif style == "fancy":
        return "\n".join([f"✨ {piece} ✨" for piece in pieces])
    else:
        raise ValueError("Stile non supportato. Scegli tra 'simple' e 'fancy'.")