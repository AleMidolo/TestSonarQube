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
        # 如果是Provides类型,直接返回
        return provides

    # 获取对象的类
    cls = getattr(object, "__class__", None)
    
    if cls is not None and getattr(cls, "__provides__", None) == provides:
        # 如果对象的类有__provides__属性,且与对象的__provides__相同
        # 说明这是从类继承来的接口声明,应该返回空
        return _empty
        
    return provides