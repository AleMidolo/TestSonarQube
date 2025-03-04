def plugins_manager(cls):
    """
    Obtiene el gestor de plugins.
    """
    if not hasattr(cls, '_plugins_manager'):
        from pineboo.plugins.manager import PluginsManager
        cls._plugins_manager = PluginsManager()
    
    return cls._plugins_manager