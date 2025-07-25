def protocol_handlers(cls, protocol_version=None):
    # Dictionary to store all available protocol handlers
    handlers = {
        (3, 0): BoltProtocolV3_0,
        (4, 0): BoltProtocolV4_0,
        (4, 1): BoltProtocolV4_1,
        (4, 2): BoltProtocolV4_2,
        (4, 3): BoltProtocolV4_3,
        (4, 4): BoltProtocolV4_4,
        (5, 0): BoltProtocolV5_0
    }

    # If no specific version requested, return all handlers
    if protocol_version is None:
        return handlers

    # Type check for protocol_version
    if not isinstance(protocol_version, tuple):
        raise TypeError("Protocol version must be a tuple")

    # If specific version requested, return only that handler if supported
    if protocol_version in handlers:
        return {protocol_version: handlers[protocol_version]}
    
    # Return empty dict if requested version not supported
    return {}