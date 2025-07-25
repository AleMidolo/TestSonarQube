def protocol_handlers(cls, protocol_version=None):
    # Dizionario che mappa le versioni del protocollo ai relativi gestori
    handlers = {
        (3, 0): BoltProtocolV3,
        (4, 0): BoltProtocolV4,
        (4, 1): BoltProtocolV4_1,
        (4, 2): BoltProtocolV4_2,
        (4, 3): BoltProtocolV4_3,
        (4, 4): BoltProtocolV4_4,
        (5, 0): BoltProtocolV5
    }

    # Se non è specificata una versione, restituisce tutti i gestori disponibili
    if protocol_version is None:
        return handlers

    # Verifica che la versione sia passata come tupla
    if not isinstance(protocol_version, tuple):
        raise TypeError("La versione del protocollo deve essere una tupla")

    # Se è specificata una versione, restituisce solo il gestore per quella versione
    # se supportata, altrimenti un dizionario vuoto
    return {protocol_version: handlers[protocol_version]} if protocol_version in handlers else {}