def plugins_manager(cls):  
    """
    Ottiene il gestore dei plugin.
    """
    if not hasattr(cls, '_plugin_manager'):
        cls._plugin_manager = cls._initialize_plugin_manager()
    return cls._plugin_manager

def _initialize_plugin_manager(cls):
    # Logica per inizializzare il gestore dei plugin
    return PluginManager()