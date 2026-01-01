def set_mode(self, mode):
    """
        Set the current work mode
        :param mode: str, working mode. only ['heat', 'cool']
        >>> thermostat.set_mode('cool')
        >>> thermostat.mode
        'cool'
        """
    if mode not in ['heat', 'cool']:
        raise ValueError("Mode must be either 'heat' or 'cool'")
    self.mode = mode