def register_vcs_handler(vcs, method):
    """
    创建一个装饰器，用于将方法标记为对象的处理器。
    创建一个装饰器，用于将方法标记为某个版本控制系统（VCS）的处理器。
    """
    def decorate(f):
        """
        创建一个装饰器，用于将方法标记为某个版本控制系统（VCS）的处理器。
        """
        if not hasattr(f, '_vcs_handlers'):
            f._vcs_handlers = {}
        f._vcs_handlers[vcs] = method
        return f
    return decorate