def render(pieces, style):
    """
    Renderiza las piezas de versión dadas en el estilo solicitado.
    
    :param pieces: Diccionario con las piezas de la versión.
    :param style: Estilo de renderización.
    :return: Cadena con la versión renderizada.
    """
    if style == "full":
        return f"{pieces['major']}.{pieces['minor']}.{pieces['patch']}"
    elif style == "short":
        return f"{pieces['major']}.{pieces['minor']}"
    elif style == "patch":
        return f"{pieces['patch']}"
    else:
        raise ValueError(f"Estilo no soportado: {style}")