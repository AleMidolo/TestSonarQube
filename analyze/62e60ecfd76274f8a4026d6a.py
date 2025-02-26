def protocol_handlers(cls, protocol_version=None):
    """
    Return a dictionary of available Bolt protocol handlers,
    keyed by version tuple. If an explicit protocol version is
    provided, the dictionary will contain either zero or one items,
    depending on whether that version is supported. If no protocol
    version is provided, all available versions will be returned.

    :param protocol_version: tuple identifying a specific protocol
        version (e.g. (3, 5)) or None
    :return: dictionary of version tuple to handler class for all
        relevant and supported protocol versions
    :raise TypeError: if protocol version is not passed in a tuple
    """
    if protocol_version is not None and not isinstance(protocol_version, tuple):
        raise TypeError("protocol_version must be a tuple")

    handlers = {
        (3, 0): "HandlerFor3_0",
        (3, 1): "HandlerFor3_1",
        (3, 2): "HandlerFor3_2",
        (3, 3): "HandlerFor3_3",
        (3, 4): "HandlerFor3_4",
        (3, 5): "HandlerFor3_5",
    }

    if protocol_version is not None:
        return {protocol_version: handlers.get(protocol_version)} if protocol_version in handlers else {}

    return handlers