def namesAndDescriptions(self, all=False):  # pylint:disable=redefined-builtin
    """
    返回当前类属性的名称和描述。
    如果all为假，则返回由接口定义的属性名称和描述。
    """
    attributes = {}
    for name, value in self.__class__.__dict__.items():
        if not name.startswith('__'):
            if not all and hasattr(value, '__is_interface__'):
                attributes[name] = value.__doc__
            elif all:
                attributes[name] = value.__doc__
    return attributes