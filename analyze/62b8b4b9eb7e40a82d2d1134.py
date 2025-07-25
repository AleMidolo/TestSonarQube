def namesAndDescriptions(self, all=False):  # pylint:disable=redefined-builtin
    """
    返回当前类属性的名称和描述。
    如果all为假，则返回由接口定义的属性名称和描述。
    """
    attributes = {}
    for name, value in self.__class__.__dict__.items():
        if not name.startswith('__'):
            if not all and not hasattr(value, '__isinterface__'):
                continue
            description = value.__doc__ if value.__doc__ else "No description available."
            attributes[name] = description
    return attributes