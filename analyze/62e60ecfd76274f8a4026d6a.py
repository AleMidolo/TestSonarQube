def protocol_handlers(cls, protocol_version=None):
    # Dictionary to store all available protocol handlers
    handlers = {
        (3, 0): "BoltProtocolV3x0",
        (3, 5): "BoltProtocolV3x5", 
        (4, 0): "BoltProtocolV4x0",
        (4, 1): "BoltProtocolV4x1",
        (4, 4): "BoltProtocolV4x4"
    }
    
    # If no specific version requested, return all handlers
    if protocol_version is None:
        return handlers
        
    # Validate protocol_version is a tuple
    if not isinstance(protocol_version, tuple):
        raise TypeError("Protocol version must be a tuple")
        
    # If specific version requested, return only that handler if supported
    if protocol_version in handlers:
        return {protocol_version: handlers[protocol_version]}
    
    # Return empty dict if version not supported
    return {}