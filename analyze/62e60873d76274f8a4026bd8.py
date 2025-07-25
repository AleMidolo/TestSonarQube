def protocol_handlers(cls, protocol_version=None):
    # 存储所有支持的协议版本和对应的处理程序
    handlers = {
        (3, 0): BoltProtocolV3,
        (4, 0): BoltProtocolV4,
        (4, 1): BoltProtocolV4_1,
        (4, 2): BoltProtocolV4_2,
        (4, 3): BoltProtocolV4_3,
        (4, 4): BoltProtocolV4_4,
        (5, 0): BoltProtocolV5
    }
    
    # 如果未指定版本,返回所有支持的处理程序
    if protocol_version is None:
        return handlers
        
    # 检查协议版本参数类型
    if not isinstance(protocol_version, tuple):
        raise TypeError("Protocol version must be specified as a tuple")
        
    # 如果指定了版本,只返回该版本的处理程序(如果支持)
    if protocol_version in handlers:
        return {protocol_version: handlers[protocol_version]}
    
    # 如果指定的版本不支持,返回空字典
    return {}