def names(self, all=False): # pylint:disable=redefined-builtin
    """
    返回当前类的属性名称。
    如果all为假，则返回接口定义的属性名称。
    """
    if all:
        # 返回所有属性名称，包括私有属性
        return [attr for attr in dir(self) if not attr.startswith('__')]
    else:
        # 只返回公共属性名称
        return [attr for attr in dir(self) if not attr.startswith('_')]