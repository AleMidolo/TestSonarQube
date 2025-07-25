def directlyProvidedBy(object):
    """
    返回由给定对象直接提供的接口
    返回值是一个 `~zope.interface.interfaces.IDeclaration`。
    provides = getattr(object, "__provides__", None)
    如果 provides 为 None，则没有指定规范。可能已经获取了 implements 规范，作为一种优化。如果是这种情况，相当于只有一个基类，我们需要将其去除，以排除类提供的声明。
    """
    provides = getattr(object, "__provides__", None)
    if provides is None:
        implements = getattr(object, "__implements__", None)
        if implements is not None and len(implements) > 0:
            # Assuming the first item is the base class we want to exclude
            return implements[1:]  # Exclude the first base class
    return provides