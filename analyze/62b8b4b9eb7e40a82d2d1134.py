def namesAndDescriptions(self, all=False): # pylint:disable=redefined-builtin
    """
    返回当前类属性的名称和描述。
    如果all为假，则返回由接口定义的属性名称和描述。
    """
    # 获取类的所有属性
    attributes = {}
    
    # 如果all为True,获取所有属性
    if all:
        for name, attr in self.__class__.__dict__.items():
            if not name.startswith('_'):  # 排除私有属性
                doc = attr.__doc__ if hasattr(attr, '__doc__') else ''
                attributes[name] = doc
    
    # 如果all为False,只获取接口定义的属性
    else:
        # 获取接口定义的属性
        if hasattr(self.__class__, '__provides__'):
            interface = self.__class__.__provides__[0]
            for name in interface:
                if not name.startswith('_'):
                    attr = getattr(self.__class__, name, None)
                    doc = attr.__doc__ if attr and hasattr(attr, '__doc__') else ''
                    attributes[name] = doc
    
    return attributes