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
    # Dictionary mapping protocol versions to their handler classes
    handlers = {
        (3, 0): BoltProtocolV3,
        (4, 0): BoltProtocolV4,
        (4, 1): BoltProtocolV4_1,
        (4, 2): BoltProtocolV4_2,
        (4, 3): BoltProtocolV4_3,
        (4, 4): BoltProtocolV4_4,
        (5, 0): BoltProtocolV5,
        (5, 1): BoltProtocolV5_1
    }

    # If no specific version requested, return all handlers
    if protocol_version is None:
        return handlers

    # Validate protocol_version is a tuple
    if not isinstance(protocol_version, tuple):
        raise TypeError("Protocol version must be specified as a tuple")

    # If specific version requested, return only that handler if supported
    if protocol_version in handlers:
        return {protocol_version: handlers[protocol_version]}
    
    # Return empty dict if requested version not supported
    return {}