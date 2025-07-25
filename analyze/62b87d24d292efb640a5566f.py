def render(pieces, style):
    """
    Renderiza las piezas de versión dadas en el estilo solicitado.
    
    :param pieces: Diccionario con las piezas de la versión.
    :param style: Estilo en el que se debe renderizar la versión.
    :return: Versión renderizada como cadena de texto.
    """
    if style == "full":
        return f"{pieces['major']}.{pieces['minor']}.{pieces['patch']}"
    elif style == "major_minor":
        return f"{pieces['major']}.{pieces['minor']}"
    elif style == "major":
        return f"{pieces['major']}"
    else:
        raise ValueError(f"Estilo no soportado: {style}")