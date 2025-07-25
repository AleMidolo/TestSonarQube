def on(self, hook):
    def decorator(func):
        if not hasattr(self, '_handlers'):
            self._handlers = {}
        if hook not in self._handlers:
            self._handlers[hook] = []
        self._handlers[hook].append(func)
        return func
    return decorator