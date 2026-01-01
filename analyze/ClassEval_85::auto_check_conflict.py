def auto_check_conflict(self):
    """
        Check if there is a conflict between the operating mode and the relationship between the current temperature and the target temperature.
        If there is a conflict, the operating mode will be adjusted automatically.
        :return: True if mode isn't conflict with the relationship between the current temperature and the target temperature, or False otherwise.
        >>> thermostat = Thermostat(20.4, 37.5, 'cool')
        >>> thermostat.auto_check_conflict()
        False
        >>> thermostat.mode
        'heat'
        """
    if self.current_temperature < self.target_temperature:
        if self.mode != 'heat':
            self.mode = 'heat'
            return False
        else:
            return True
    elif self.current_temperature > self.target_temperature:
        if self.mode != 'cool':
            self.mode = 'cool'
            return False
        else:
            return True
    else:
        return True