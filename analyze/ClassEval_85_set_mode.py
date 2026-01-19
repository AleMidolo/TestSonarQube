def set_mode(self, mode):
    """
    Ottieni l'attuale modalità di lavoro
    :param mode: str, modalità di lavoro. solo ['heat', 'cool']
    >>> thermostat.set_mode('cool')
    >>> thermostat.mode
    'cool'
    """
    if mode in ['heat', 'cool']:
        self.mode = mode
    else:
        raise ValueError("Mode must be either 'heat' or 'cool'")