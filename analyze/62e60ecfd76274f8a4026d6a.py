def protocol_handlers(cls, protocol_version=None):
    if protocol_version is not None and not isinstance(protocol_version, tuple):
        raise TypeError("La versione del protocollo deve essere passata come una tupla")

    handlers = {
        (3, 5): "HandlerFor3_5",
        (4, 0): "HandlerFor4_0",
        (4, 1): "HandlerFor4_1",
    }

    if protocol_version is not None:
        return {protocol_version: handlers.get(protocol_version)} if protocol_version in handlers else {}

    return handlers