def protocol_handlers(cls, protocol_version=None):
    """
    Devuelve un diccionario de los controladores de protocolo Bolt disponibles, indexados por una tupla de versión. Si se proporciona una versión de protocolo explícita, el diccionario contendrá cero o un elemento, dependiendo de si esa versión es compatible. Si no se proporciona ninguna versión de protocolo, se devolverán todas las versiones disponibles.

    :param protocol_version: tupla que identifica una versión específica del protocolo (por ejemplo, (3, 5)) o None
    :return: diccionario que mapea tuplas de versión a clases de controladores para todas las versiones relevantes y compatibles del protocolo
    :raise TypeError: si la versión del protocolo no se pasa como una tupla
    """
    if protocol_version is not None and not isinstance(protocol_version, tuple):
        raise TypeError("La versión del protocolo debe ser una tupla")

    # Simulación de controladores de protocolo disponibles
    available_handlers = {
        (3, 0): "HandlerV3_0",
        (3, 5): "HandlerV3_5",
        (4, 0): "HandlerV4_0",
    }

    if protocol_version is not None:
        return {protocol_version: available_handlers.get(protocol_version)} if protocol_version in available_handlers else {}

    return available_handlers