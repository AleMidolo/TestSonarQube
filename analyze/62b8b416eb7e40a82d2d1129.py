def names(self, all=False):  # pylint:disable=redefined-builtin
    """
    返回当前类的属性名称。
    如果all为假，则返回接口定义的属性名称。
    """
    if all:
        return [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]
    else:
        return [attr for attr in self.__dict__.keys() if not callable(getattr(self, attr)) and not attr.startswith("__")]