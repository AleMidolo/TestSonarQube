def on(self, hook):
    """
    Decorator function to add a new handler to the registry.

    Args:
        hook (HookType): Hook attribute for which to register the handler.

    Returns:
        callable: Decorator for registering listeners for the specified
        hook.
    """
    def decorator(handler):
        if hook not in self._handlers:
            self._handlers[hook] = []
        self._handlers[hook].append(handler)
        return handler
    return decorator