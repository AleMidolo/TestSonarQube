def auto_set_mode(self):
    """
        Automatically set the operating mode based on the comparison of current temperature and target temperature.
        If the current temperature is less than the target temperature, the operating mode is set to 'heat', otherwise it is set to 'cool'.
        >>> thermostat = Thermostat(20.4, 37.5, 'cool')
        >>> thermostat.auto_set_mode()
        >>> thermostat.mode
        'heat'
        """
    if self.current_temperature < self.target_temperature:
        self.mode = 'heat'
    else:
        self.mode = 'cool'