def register_vcs_handler(vcs, method):
    """
    创建一个装饰器，用于将方法标记为某个版本控制系统（VCS）的处理器。
    
    :param vcs: 版本控制系统的名称
    :param method: 处理器的名称
    :return: 装饰器函数
    """
    def decorate(f):
        """
        创建一个装饰器，用于将方法标记为某个版本控制系统（VCS）的处理器。
        
        :param f: 被装饰的函数
        :return: 装饰后的函数
        """
        if not hasattr(f, '_vcs_handlers'):
            f._vcs_handlers = {}
        f._vcs_handlers[vcs] = method
        return f
    return decorate