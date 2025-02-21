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

    handlers = {
        (3, 5): "Handler35",
        (4, 0): "Handler40",
        (4, 1): "Handler41",
        # Aggiungere altri gestori di protocollo qui
    }

    if protocol_version is not None:
        return {protocol_version: handlers.get(protocol_version)} if protocol_version in handlers else {}

    return handlers