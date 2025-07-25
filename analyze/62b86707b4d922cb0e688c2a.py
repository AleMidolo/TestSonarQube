def on(self, hook):
    def decorator(handler):
        if hook not in self._registry:
            self._registry[hook] = []
        self._registry[hook].append(handler)
        return handler
    return decorator