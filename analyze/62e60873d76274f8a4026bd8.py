def protocol_handlers(cls, protocol_version=None):
    """
    Restituisce un dizionario dei gestori di protocollo Bolt disponibili,
    indicizzati per tuple di versione. Se viene fornita una versione di protocollo
    esplicita, il dizionario conterrà zero o un elemento, a seconda che quella
    versione sia supportata o meno. Se non viene fornita alcuna versione di protocollo,
    verranno restituite tutte le versioni disponibili.

    :param protocol_version: tupla che identifica una specifica versione
        del protocollo (ad esempio, (3, 5)) oppure None
    :return: dizionario che associa una tupla di versione alla classe del gestore
        per tutte le versioni di protocollo rilevanti e supportate
    :raise TypeError: se la versione del protocollo non è passata come una tupla
    """
    # Dizionario che mappa le versioni del protocollo ai relativi gestori
    handlers = {
        (1, 0): BoltProtocolV1Handler,
        (2, 0): BoltProtocolV2Handler, 
        (3, 0): BoltProtocolV3Handler,
        (4, 0): BoltProtocolV4Handler,
        (4, 1): BoltProtocolV4_1Handler,
        (4, 2): BoltProtocolV4_2Handler,
        (4, 3): BoltProtocolV4_3Handler,
        (4, 4): BoltProtocolV4_4Handler,
        (5, 0): BoltProtocolV5Handler
    }

    if protocol_version is not None:
        # Verifica che la versione del protocollo sia una tupla
        if not isinstance(protocol_version, tuple):
            raise TypeError("La versione del protocollo deve essere specificata come tupla")
            
        # Se è stata specificata una versione, restituisce solo il gestore per quella versione
        if protocol_version in handlers:
            return {protocol_version: handlers[protocol_version]}
        return {}
    
    # Se non è stata specificata una versione, restituisce tutti i gestori disponibili
    return handlers