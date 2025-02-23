def plugins_manager(cls):  
    """
    Ottiene il gestore dei plugin.
    """
    # Assuming we have a PluginManager class that handles plugins
    class PluginManager:
        def __init__(self):
            self.plugins = []

        def load_plugin(self, plugin):
            self.plugins.append(plugin)

        def get_plugins(self):
            return self.plugins

    # Create an instance of PluginManager and return it
    return PluginManager()