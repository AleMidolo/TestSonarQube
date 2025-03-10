def protocol_handlers(cls, protocol_version=None):
    """
    Devuelve un diccionario de los controladores de protocolo Bolt disponibles, indexados por una tupla de versión. Si se proporciona una versión de protocolo explícita, el diccionario contendrá cero o un elemento, dependiendo de si esa versión es compatible. Si no se proporciona ninguna versión de protocolo, se devolverán todas las versiones disponibles.

    :param protocol_version: tupla que identifica una versión específica del protocolo (por ejemplo, (3, 5)) o None
    :return: diccionario que mapea tuplas de versión a clases de controladores para todas las versiones relevantes y compatibles del protocolo
    :raise TypeError: si la versión del protocolo no se pasa como una tupla
    """
    # Diccionario de controladores de protocolo Bolt disponibles
    available_handlers = {
        (3, 5): cls.BoltV3_5Handler,
        (4, 0): cls.BoltV4_0Handler,
        (4, 1): cls.BoltV4_1Handler,
        # Agrega más versiones y controladores según sea necesario
    }

    if protocol_version is not None:
        if not isinstance(protocol_version, tuple):
            raise TypeError("La versión del protocolo debe ser una tupla.")
        # Filtra el diccionario para incluir solo la versión especificada
        return {protocol_version: available_handlers.get(protocol_version)}
    else:
        # Devuelve todos los controladores disponibles
        return available_handlers