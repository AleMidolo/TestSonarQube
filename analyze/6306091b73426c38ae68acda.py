def plugins_manager(cls):
    """
    Gets the plugin manager.
    """
    if not hasattr(cls, '_plugins_manager'):
        cls._plugins_manager = PluginManager()
    return cls._plugins_manager