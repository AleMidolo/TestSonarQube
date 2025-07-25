def on(self, hook):
    """
    Decorator function to add a new handler to the registry.

    Args:
        hook (HookType): Hook attribute for which to register the handler.

    Returns:
        callable: Decorator for registering listeners for the specified
        hook.
    """
    def decorator(func):
        if not hasattr(self, '_registry'):
            self._registry = {}
        if hook not in self._registry:
            self._registry[hook] = []
        self._registry[hook].append(func)
        return func
    return decorator