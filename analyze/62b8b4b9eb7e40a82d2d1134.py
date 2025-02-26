def namesAndDescriptions(self, all=False): # pylint:disable=redefined-builtin
    """
    返回当前类属性的名称和描述。
    如果all为假，则返回由接口定义的属性名称和描述。
    """
    if all:
        return {attr: getattr(self, attr).__doc__ for attr in dir(self) if not attr.startswith('_')}
    else:
        return {attr: getattr(self, attr).__doc__ for attr in self.__class__.__dict__ if not attr.startswith('_')}