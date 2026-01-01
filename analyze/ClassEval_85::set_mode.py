def set_mode(self, mode):
    """
        Obtener el modo de trabajo actual
        :param mode: str, modo de trabajo. solo ['heat', 'cool']
        >>> thermostat.set_mode('cool')
        >>> thermostat.mode
        'cool'
        """
    if mode not in ['heat', 'cool']:
        raise ValueError("Mode must be either 'heat' or 'cool'")
    self.mode = mode