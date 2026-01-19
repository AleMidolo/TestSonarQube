def auto_set_mode(self):
    """
    Establece automáticamente el modo de operación comparando la temperatura actual con la temperatura objetivo. Si la temperatura actual es inferior a la temperatura objetivo, el modo de operación se establece en 'calor', de lo contrario se establece en 'frío'.
    >>> thermostat = Thermostat(20.4, 37.5, 'frío')
    >>> thermostat.auto_set_mode()
    >>> thermostat.mode
    'calor'
    """
    if self.current_temperature < self.target_temperature:
        self.mode = 'calor'
    else:
        self.mode = 'frío'