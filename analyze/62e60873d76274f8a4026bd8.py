def protocol_handlers(cls, protocol_version=None):
    # Diccionario con los controladores disponibles
    handlers = {
        (3, 0): BoltProtocolV3,
        (4, 0): BoltProtocolV4,
        (4, 1): BoltProtocolV4_1,
        (4, 2): BoltProtocolV4_2,
        (4, 3): BoltProtocolV4_3,
        (4, 4): BoltProtocolV4_4,
        (5, 0): BoltProtocolV5
    }

    # Si no se especifica versión, devolver todos los handlers
    if protocol_version is None:
        return handlers

    # Validar que la versión sea una tupla
    if not isinstance(protocol_version, tuple):
        raise TypeError("La versión del protocolo debe ser una tupla")

    # Si se especifica versión, devolver solo el handler correspondiente
    filtered_handlers = {}
    if protocol_version in handlers:
        filtered_handlers[protocol_version] = handlers[protocol_version]

    return filtered_handlers