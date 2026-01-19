def set_target_temperature(self, temperature):
    """
        Establecer la temperatura objetivo
        :param temperature: float, la temperatura objetivo
        >>> thermostat.set_target_temperature(37.6)
        >>> thermostat.target_temperature
        37.6
        """
    self.target_temperature = temperature