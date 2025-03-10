def render(pieces, style):
    """
    Renderiza las piezas de versión dadas en el estilo solicitado.
    """
    if style == "full":
        return f"{pieces['major']}.{pieces['minor']}.{pieces['patch']}"
    elif style == "short":
        return f"{pieces['major']}.{pieces['minor']}"
    elif style == "patch":
        return f"{pieces['patch']}"
    else:
        raise ValueError("Estilo no soportado")