def on(self, hook):
    def decorator(func):
        if not hasattr(self, '_listeners'):
            self._listeners = {}
        if hook not in self._listeners:
            self._listeners[hook] = []
        self._listeners[hook].append(func)
        return func
    return decorator