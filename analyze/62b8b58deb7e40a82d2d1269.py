def directlyProvidedBy(object):
    """
    返回由给定对象直接提供的接口
    返回值是一个 `~zope.interface.interfaces.IDeclaration`。
    provides = getattr(object, "__provides__", None)
    如果 provides 为 None，则没有指定规范。可能已经获取了 implements 规范，作为一种优化。如果是这种情况，相当于只有一个基类，我们需要将其去除，以排除类提供的声明。
    """
    provides = getattr(object, "__provides__", None)
    
    if provides is None:
        # 如果对象没有__provides__属性
        return _empty
        
    # 如果对象有__provides__属性
    if isinstance(provides, Provides):
        # 如果provides是Provides类的实例,直接返回
        return provides

    # 获取对象的类
    cls = object.__class__
    
    # 获取类的implements规范
    implements = implementedBy(cls)
    
    if provides == implements:
        # 如果provides等于implements,说明没有直接提供的接口
        return _empty
        
    # 返回provides减去implements的结果
    return provides - implements