def plugins_manager(cls):
    """
    Obtiene el gestor de plugins.
    """
    # Assuming we have a PluginManager class that handles plugins
    if not hasattr(cls, '_plugin_manager'):
        cls._plugin_manager = PluginManager()
    return cls._plugin_manager