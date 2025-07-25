def subclasses(cls):
    """
    递归地返回一个类的所有子类。
    """
    all_subclasses = []
    
    for subclass in cls.__subclasses__():
        all_subclasses.append(subclass)
        all_subclasses.extend(subclasses(subclass))
    
    return all_subclasses