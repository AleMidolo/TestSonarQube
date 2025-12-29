def get_target_temperature(self):
    """
        Get the target temperature of an instance of the Thermostat class.
        :return self.current_temperature: int
        >>> thermostat.get_target_temperature()
        37.5
        """
    return self.target_temperature