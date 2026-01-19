def simulate_operation(self):
    """
    simulate the operation of Thermostat. It will automatically start the auto_set_mode method to set the operating mode,
    and then automatically adjust the current temperature according to the operating mode until the target temperature is reached.
    :return time: int, the time it took to complete the simulation.
    >>> thermostat = Thermostat(20.4, 37.5, 'cool')
    >>> thermostat.simulate_operation()
    18
    """
    # Set the operating mode automatically
    self.auto_set_mode()
    
    time = 0
    
    # Continue adjusting temperature until target is reached
    while self.current_temp != self.target_temp:
        if self.mode == 'cool':
            # Cooling: decrease temperature
            if self.current_temp > self.target_temp:
                self.current_temp -= 1
                time += 1
            else:
                break
        elif self.mode == 'heat':
            # Heating: increase temperature
            if self.current_temp < self.target_temp:
                self.current_temp += 1
                time += 1
            else:
                break
        else:
            # Mode is 'off' or unknown, no adjustment
            break
    
    return time