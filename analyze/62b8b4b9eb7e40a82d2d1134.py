def namesAndDescriptions(self, all=False): # pylint:disable=redefined-builtin
    """
    返回当前类属性的名称和描述。
    如果all为假，则返回由接口定义的属性名称和描述。
    """
    # 获取类的所有属性
    attributes = {}
    
    if all:
        # 获取所有属性,包括继承的
        for name, attr in self.__class__.__dict__.items():
            if not name.startswith('_'):  # 排除私有属性
                doc = getattr(attr, '__doc__', None)
                attributes[name] = doc or ''
    else:
        # 只获取接口定义的属性
        for name in dir(self):
            if not name.startswith('_'):  # 排除私有属性
                attr = getattr(self, name)
                if hasattr(attr, '__doc__'):
                    attributes[name] = attr.__doc__ or ''
                    
    return attributes