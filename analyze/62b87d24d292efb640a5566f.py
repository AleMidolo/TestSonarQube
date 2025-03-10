def render(pieces, style):
    """
    Renderiza las piezas de versión dadas en el estilo solicitado.
    
    :param pieces: Diccionario con las piezas de la versión.
    :param style: Estilo de renderizado (por ejemplo, 'full', 'short', etc.).
    :return: Versión renderizada como cadena de texto.
    """
    if style == 'full':
        return f"{pieces['major']}.{pieces['minor']}.{pieces['patch']}"
    elif style == 'short':
        return f"{pieces['major']}.{pieces['minor']}"
    elif style == 'patch':
        return f"{pieces['patch']}"
    else:
        raise ValueError(f"Estilo '{style}' no soportado.")