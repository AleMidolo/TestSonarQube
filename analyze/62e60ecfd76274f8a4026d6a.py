def protocol_handlers(cls, protocol_version=None):
    # Diccionario que mapea versiones de protocolo a sus manejadores
    handlers = {
        (3, 0): BoltProtocolV3Handler,
        (4, 0): BoltProtocolV4Handler,
        (4, 1): BoltProtocolV41Handler,
        (4, 2): BoltProtocolV42Handler,
        (4, 3): BoltProtocolV43Handler,
        (4, 4): BoltProtocolV44Handler,
        (5, 0): BoltProtocolV5Handler
    }

    # Si no se especifica versión, devolver todos los manejadores
    if protocol_version is None:
        return handlers

    # Validar que la versión sea una tupla
    if not isinstance(protocol_version, tuple):
        raise TypeError("La versión del protocolo debe ser una tupla")

    # Si se especifica una versión, devolver solo ese manejador si existe
    if protocol_version in handlers:
        return {protocol_version: handlers[protocol_version]}
    
    # Si la versión no existe, devolver diccionario vacío
    return {}