def plugins_manager(cls):
    """
    Gets the plugin manager.
    """
    if not hasattr(cls, '_plugin_manager'):
        cls._plugin_manager = cls.create_plugin_manager()
    return cls._plugin_manager