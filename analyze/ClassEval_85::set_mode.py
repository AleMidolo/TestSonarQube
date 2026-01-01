def set_mode(self, mode):
    """
        Obtener el modo de trabajo actual
        :param mode: str, modo de trabajo. solo ['heat', 'cool']
        >>> thermostat.set_mode('cool')
        >>> thermostat.mode
        'cool'
        """
    if mode in ['heat', 'cool']:
        self.mode = mode