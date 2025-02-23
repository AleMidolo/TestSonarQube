def subclasses(cls):
    """
    递归地返回一个类的所有子类。
    """
    all_subclasses = set()

    def find_subclasses(c):
        for subclass in c.__subclasses__():
            all_subclasses.add(subclass)
            find_subclasses(subclass)

    find_subclasses(cls)
    return all_subclasses