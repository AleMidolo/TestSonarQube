def set_target_temperature(self, temperature):
        """
        Imposta la temperatura target
        :param temperature: float, la temperatura target
        >>> thermostat.set_target_temperature(37.6)
        >>> thermostat.target_temperature
        37.6
        """
        self.target_temperature = temperature