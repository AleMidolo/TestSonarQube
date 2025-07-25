def protocol_handlers(cls, protocol_version=None):
    """
    Restituisce un dizionario dei gestori del protocollo Bolt disponibili, indicizzati da una tupla che rappresenta la versione. 
    Se viene fornita una versione di protocollo esplicita, il dizionario conterrà zero o un elemento, a seconda che quella versione sia supportata o meno. 
    Se non viene fornita alcuna versione di protocollo, verranno restituite tutte le versioni disponibili.

    :param protocol_version: tupla che identifica una specifica versione del protocollo
        (ad esempio, (3, 5)) oppure None
    :return: dizionario che associa tuple di versione alla classe del gestore per tutte
        le versioni del protocollo rilevanti e supportate
    :raise TypeError: se la versione del protocollo non è passata come una tupla
    """
    # Esempio di gestori del protocollo supportati
    supported_handlers = {
        (3, 5): cls.BoltV3_5Handler,
        (4, 0): cls.BoltV4_0Handler,
        (4, 1): cls.BoltV4_1Handler,
    }

    if protocol_version is not None:
        if not isinstance(protocol_version, tuple):
            raise TypeError("La versione del protocollo deve essere una tupla.")
        if protocol_version in supported_handlers:
            return {protocol_version: supported_handlers[protocol_version]}
        else:
            return {}
    else:
        return supported_handlers