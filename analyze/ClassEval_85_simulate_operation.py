def simulate_operation(self):
    """
        simulate the operation of Thermostat. It will automatically start the auto_set_mode method to set the operating mode,
        and then automatically adjust the current temperature according to the operating mode until the target temperature is reached.
        :return time: int, the time it took to complete the simulation.
        >>> thermostat = Thermostat(20.4, 37.5, 'cool')
        >>> thermostat.simulate_operation()
        18
        """
    self.auto_set_mode()
    time_elapsed = 0
    while abs(self.current_temperature - self.target_temperature) > 0.1:
        if self.mode == 'heat':
            self.current_temperature += 1.0
        else:
            self.current_temperature -= 1.0
        time_elapsed += 1
        time.sleep(0.01)
    return time_elapsed