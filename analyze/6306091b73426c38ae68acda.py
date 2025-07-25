def plugins_manager(cls):
    """
    प्लगइन मैनेजर प्राप्त करता है।
    """
    class PluginManager:
        def __init__(self):
            self.plugins = []

        def register_plugin(self, plugin):
            self.plugins.append(plugin)

        def get_plugins(self):
            return self.plugins

    cls.plugin_manager = PluginManager()
    return cls