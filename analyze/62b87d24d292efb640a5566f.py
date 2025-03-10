def render(pieces, style):
    """
    Renderiza las piezas de versión dadas en el estilo solicitado.
    
    :param pieces: Lista de piezas de versión.
    :param style: Estilo de renderizado.
    :return: Versión renderizada como cadena.
    """
    if style == "full":
        return ".".join(map(str, pieces))
    elif style == "short":
        return ".".join(map(str, pieces[:2]))
    elif style == "compact":
        return "".join(map(str, pieces))
    else:
        raise ValueError(f"Estilo no soportado: {style}")