def protocol_handlers(cls, protocol_version=None):
    """
    Restituisce un dizionario dei gestori del protocollo Bolt disponibili, indicizzati da una tupla che rappresenta la versione. Se viene fornita una versione di protocollo esplicita, il dizionario conterrà zero o un elemento, a seconda che quella versione sia supportata o meno. Se non viene fornita alcuna versione di protocollo, verranno restituite tutte le versioni disponibili.

    :param protocol_version: tupla che identifica una specifica versione del protocollo
        (ad esempio, (3, 5)) oppure None
    :return: dizionario che associa tuple di versione alla classe del gestore per tutte
        le versioni del protocollo rilevanti e supportate
    :raise TypeError: se la versione del protocollo non è passata come una tupla
    """
    if protocol_version is not None and not isinstance(protocol_version, tuple):
        raise TypeError("La versione del protocollo deve essere passata come una tupla")

    # Simulazione di un dizionario di gestori del protocollo
    protocol_handlers_dict = {
        (3, 0): "HandlerV3_0",
        (3, 1): "HandlerV3_1",
        (3, 2): "HandlerV3_2",
        (3, 5): "HandlerV3_5",
        (4, 0): "HandlerV4_0",
    }

    if protocol_version is not None:
        return {protocol_version: protocol_handlers_dict.get(protocol_version)} if protocol_version in protocol_handlers_dict else {}

    return protocol_handlers_dict