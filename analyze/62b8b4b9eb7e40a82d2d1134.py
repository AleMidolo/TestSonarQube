def namesAndDescriptions(self, all=False): # pylint:disable=redefined-builtin
    """
    返回当前类属性的名称和描述。
    如果all为假，则返回由接口定义的属性名称和描述。
    """
    # 获取类的所有属性
    attributes = {}
    
    # 如果all为True,获取所有属性
    if all:
        for name in dir(self):
            # 跳过私有属性
            if name.startswith('_'):
                continue
            attr = getattr(self, name)
            # 获取属性的文档字符串作为描述
            desc = getattr(attr, '__doc__', None)
            if desc is None:
                desc = ''
            attributes[name] = desc
            
    # 如果all为False,只获取接口定义的属性
    else:
        # 获取类实现的接口
        for interface in getattr(self.__class__, '__bases__', []):
            for name in dir(interface):
                if name.startswith('_'):
                    continue
                attr = getattr(interface, name)
                desc = getattr(attr, '__doc__', None)
                if desc is None:
                    desc = ''
                attributes[name] = desc
                
    return attributes