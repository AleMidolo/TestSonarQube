def protocol_handlers(cls, protocol_version=None):
    # Check if protocol_version is a tuple when provided
    if protocol_version is not None and not isinstance(protocol_version, tuple):
        raise TypeError("Protocol version must be specified as a tuple")
        
    # Get all handlers registered with the class
    handlers = getattr(cls, "_protocol_handlers", {})
    
    if protocol_version is None:
        # Return all available handlers if no specific version requested
        return handlers
    else:
        # Return handler for specific version if it exists, otherwise empty dict
        return {protocol_version: handlers[protocol_version]} if protocol_version in handlers else {}