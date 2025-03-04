def plugins_manager(cls):
    """
    प्लगइन मैनेजर प्राप्त करता है।
    """
    if not hasattr(cls, '_plugins_manager'):
        from yapsy.PluginManager import PluginManager
        cls._plugins_manager = PluginManager()
        cls._plugins_manager.setPluginPlaces(['plugins'])
        cls._plugins_manager.collectPlugins()
    return cls._plugins_manager