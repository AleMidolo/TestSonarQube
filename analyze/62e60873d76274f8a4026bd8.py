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
    if protocol_version is not None and not isinstance(protocol_version, tuple):
        raise TypeError("La versione del protocollo deve essere una tupla.")

    # Simulazione di un dizionario di gestori di protocollo
    protocol_handlers_dict = {
        (3, 0): "HandlerV3_0",
        (3, 1): "HandlerV3_1",
        (3, 5): "HandlerV3_5",
        (4, 0): "HandlerV4_0",
    }

    if protocol_version is not None:
        return {protocol_version: protocol_handlers_dict.get(protocol_version)}
    
    return protocol_handlers_dict