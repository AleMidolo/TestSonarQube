def protocol_handlers(cls, protocol_version=None):
    if protocol_version is not None and not isinstance(protocol_version, tuple):
        raise TypeError("protocol version must be a tuple")
    
    handlers = {
        (3, 0): 'HandlerV3_0',
        (3, 1): 'HandlerV3_1',
        (3, 2): 'HandlerV3_2',
        (3, 3): 'HandlerV3_3',
        (3, 4): 'HandlerV3_4',
        (3, 5): 'HandlerV3_5',
    }
    
    if protocol_version is not None:
        return {protocol_version: handlers.get(protocol_version)} if protocol_version in handlers else {}
    
    return handlers