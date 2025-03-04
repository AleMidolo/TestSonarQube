def protocol_handlers(cls, protocol_version=None):
    # Check if protocol_version is a tuple when provided
    if protocol_version is not None and not isinstance(protocol_version, tuple):
        raise TypeError("Protocol version must be specified as a tuple")

    # Get all handlers registered with the class
    handlers = {version: handler for version, handler in cls.__dict__.items() 
               if isinstance(version, tuple)}

    # If specific version requested, return only that handler if it exists
    if protocol_version is not None:
        return {protocol_version: handlers.get(protocol_version)} if protocol_version in handlers else {}

    # Otherwise return all handlers
    return handlers