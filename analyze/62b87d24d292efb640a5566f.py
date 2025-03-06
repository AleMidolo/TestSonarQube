def render(pieces, style):
    """
    Renderiza las piezas de versión dadas en el estilo solicitado.
    """
    if style == "full":
        return f"{pieces['major']}.{pieces['minor']}.{pieces['patch']}"
    elif style == "major":
        return f"{pieces['major']}"
    elif style == "minor":
        return f"{pieces['major']}.{pieces['minor']}"
    elif style == "patch":
        return f"{pieces['major']}.{pieces['minor']}.{pieces['patch']}"
    else:
        raise ValueError(f"Estilo no soportado: {style}")