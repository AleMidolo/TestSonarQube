def on(self, hook):
    """
    返回一个装饰器函数，用于向类中的注册表中的 "hook" 添加一个新的处理器。

    该装饰器函数用于向注册表中添加一个新的处理器。

    参数：
      hook (HookType): 要为其注册处理器的 Hook 属性。

    返回值：
      callable: 用于为指定的 hook 注册监听器的装饰器。
    """
    def decorator(func):
        if hook not in self._registry:
            self._registry[hook] = []
        self._registry[hook].append(func)
        return func
    return decorator