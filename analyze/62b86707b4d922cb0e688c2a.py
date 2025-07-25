def on(self, hook):
    def decorator(listener):
        if hook not in self._listeners:
            self._listeners[hook] = []
        self._listeners[hook].append(listener)
        return listener
    return decorator