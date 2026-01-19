def set_target_temperature(self, temperature):
    """
        लक्षित तापमान सेट करें
        :param temperature: float, लक्षित तापमान
        >>> thermostat.set_target_temperature(37.6)
        >>> thermostat.target_temperature
        37.6
        """
    self.target_temperature = temperature