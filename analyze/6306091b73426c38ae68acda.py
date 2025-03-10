def plugins_manager(cls):
    """
    प्लगइन मैनेजर प्राप्त करता है।
    """
    # Assuming the plugin manager is a class attribute or method
    if hasattr(cls, 'get_plugin_manager'):
        return cls.get_plugin_manager()
    else:
        raise AttributeError(f"{cls.__name__} has no attribute 'get_plugin_manager'")