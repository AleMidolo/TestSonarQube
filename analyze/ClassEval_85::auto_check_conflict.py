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
        if (self.current_temperature < self.target_temperature and self.mode == 'cool') or \
           (self.current_temperature > self.target_temperature and self.mode == 'heat'):
            self.auto_set_mode()
            return False
        return True