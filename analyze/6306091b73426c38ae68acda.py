def plugins_manager(cls):
    """
    Obtiene el gestor de plugins.
    """
    if not hasattr(cls, '_plugins_manager'):
        from pineboolib.plugins.manager import PluginManager
        cls._plugins_manager = PluginManager()
    
    return cls._plugins_manager