def plugins_manager(cls):  
    """
    Ottiene il gestore dei plugin.
    """
    if not hasattr(cls, '_plugin_manager'):
        cls._plugin_manager = {}
    return cls._plugin_manager