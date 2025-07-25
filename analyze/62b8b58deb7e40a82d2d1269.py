def directlyProvidedBy(object):
    """
    返回由给定对象直接提供的接口
    返回值是一个 `~zope.interface.interfaces.IDeclaration`。
    provides = getattr(object, "__provides__", None)
    如果 provides 为 None，则没有指定规范。可能已经获取了 implements 规范，作为一种优化。如果是这种情况，相当于只有一个基类，我们需要将其去除，以排除类提供的声明。
    """
    provides = getattr(object, "__provides__", None)
    if provides is None:
        # 如果没有指定规范，尝试获取 implements 规范
        implements = getattr(object, "__implemented__", None)
        if implements is not None:
            # 如果只有一个基类，去除它以排除类提供的声明
            if len(implements) == 1:
                return None
            else:
                return implements
        else:
            return None
    else:
        return provides