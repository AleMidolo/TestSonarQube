def protocol_handlers(cls, protocol_version=None):
    if protocol_version is not None and not isinstance(protocol_version, tuple):
        raise TypeError("protocol_version must be a tuple")
    
    available_handlers = {
        (3, 0): 'HandlerV3_0',
        (3, 1): 'HandlerV3_1',
        (3, 5): 'HandlerV3_5',
        (4, 0): 'HandlerV4_0',
    }
    
    if protocol_version is not None:
        return {protocol_version: available_handlers.get(protocol_version)} if protocol_version in available_handlers else {}
    
    return available_handlers