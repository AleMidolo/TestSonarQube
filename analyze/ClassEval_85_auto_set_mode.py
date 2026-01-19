def auto_set_mode(self):
    """
    Imposta automaticamente la modalità operativa confrontando la temperatura attuale con la temperatura target. Se la temperatura attuale è inferiore alla temperatura target, la modalità operativa viene impostata su 'heat', altrimenti viene impostata su 'cool'.
    >>> thermostat = Thermostat(20.4, 37.5, 'cool')
    >>> thermostat.auto_set_mode()
    >>> thermostat.mode
    'heat'
    """
    if self.current_temperature < self.target_temperature:
        self.mode = 'heat'
    else:
        self.mode = 'cool'