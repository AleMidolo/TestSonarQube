def protocol_handlers(cls, protocol_version=None):
    """
    Restituisce un dizionario dei gestori del protocollo Bolt disponibili, indicizzati da una tupla che rappresenta la versione. Se viene fornita una versione di protocollo esplicita, il dizionario conterrà zero o un elemento, a seconda che quella versione sia supportata o meno. Se non viene fornita alcuna versione di protocollo, verranno restituite tutte le versioni disponibili.

    :param protocol_version: tupla che identifica una specifica versione del protocollo
        (ad esempio, (3, 5)) oppure None
    :return: dizionario che associa tuple di versione alla classe del gestore per tutte
        le versioni del protocollo rilevanti e supportate
    :raise TypeError: se la versione del protocollo non è passata come una tupla
    """
    # Esempio di gestori di protocollo disponibili
    available_handlers = {
        (3, 5): "Bolt3_5Handler",
        (4, 0): "Bolt4_0Handler",
        (4, 1): "Bolt4_1Handler",
    }

    if protocol_version is not None:
        if not isinstance(protocol_version, tuple):
            raise TypeError("La versione del protocollo deve essere una tupla.")
        if protocol_version in available_handlers:
            return {protocol_version: available_handlers[protocol_version]}
        else:
            return {}
    else:
        return available_handlers