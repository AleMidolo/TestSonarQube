def set_mode(self, mode):
    """
    Get the current work mode
    :param mode: str, working mode. only ['heat', 'cool']
    >>> thermostat.set_mode('cool')
    >>> thermostat.mode
    'cool'
    """
    if mode in ['heat', 'cool']:
        self.mode = mode