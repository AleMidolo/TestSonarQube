def plugins_manager(cls):
    """
    Ottiene il gestore dei plugin.
    """
    if not hasattr(cls, '_plugins_manager'):
        from plugins.manager import PluginsManager
        cls._plugins_manager = PluginsManager()
    return cls._plugins_manager