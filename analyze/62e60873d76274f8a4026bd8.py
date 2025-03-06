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
    # Dizionario delle versioni supportate e dei loro gestori
    supported_versions = {
        (3, 5): cls.BoltHandlerV3_5,
        (4, 0): cls.BoltHandlerV4_0,
        (4, 1): cls.BoltHandlerV4_1,
        # Aggiungi altre versioni supportate qui
    }

    if protocol_version is not None:
        if not isinstance(protocol_version, tuple):
            raise TypeError("La versione del protocollo deve essere una tupla.")
        if protocol_version in supported_versions:
            return {protocol_version: supported_versions[protocol_version]}
        else:
            return {}
    else:
        return supported_versions