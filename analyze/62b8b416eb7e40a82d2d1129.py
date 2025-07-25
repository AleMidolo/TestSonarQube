def names(self, all=False):  # pylint:disable=redefined-builtin
    """
    返回当前类的属性名称。
    如果all为假，则返回接口定义的属性名称。
    """
    if all:
        return [name for name in dir(self) if not name.startswith('__')]
    else:
        return [name for name in dir(self.__class__) if not name.startswith('__')]