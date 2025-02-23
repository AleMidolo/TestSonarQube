def plugins_manager(cls):
    """
    प्लगइन मैनेजर प्राप्त करता है।
    """
    class PluginManager:
        def __init__(self):
            self.plugins = []

        def load_plugin(self, plugin):
            self.plugins.append(plugin)

        def unload_plugin(self, plugin):
            self.plugins.remove(plugin)

        def list_plugins(self):
            return self.plugins

    cls.plugin_manager = PluginManager()
    return cls