def set_mode(self, mode):
    """
        Ottieni l'attuale modalità di lavoro
        :param mode: str, modalità di lavoro. solo ['heat', 'cool']
        >>> thermostat.set_mode('cool')
        >>> thermostat.mode
        'cool'
        """
    self.mode = mode