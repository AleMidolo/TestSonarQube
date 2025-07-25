def plugins_manager(cls):
    """
    Ottiene il gestore dei plugin.
    """
    # Assuming the plugin manager is a class attribute or method
    # This is a placeholder implementation
    if hasattr(cls, '_plugin_manager'):
        return cls._plugin_manager
    else:
        raise AttributeError("Plugin manager not found in the class.")