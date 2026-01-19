def simulate_operation(self):
    """
    simulate the operation of Thermostat. It will automatically start the auto_set_mode method to set the operating mode,
    and then automatically adjust the current temperature according to the operating mode until the target temperature is reached.
    :return time: int, the time it took to complete the simulation.
    >>> thermostat = Thermostat(20.4, 37.5, 'cool')
    >>> thermostat.simulate_operation()
    18
    """
    time = 0
    self.auto_set_mode()
    
    while self.current_temp != self.target_temp:
        if self.mode == 'cool':
            if self.current_temp > self.target_temp:
                self.current_temp -= 0.5
            else:
                break
        elif self.mode == 'heat':
            if self.current_temp < self.target_temp:
                self.current_temp += 0.5
            else:
                break
        else:  # mode == 'idle'
            break
        
        time += 1
    
    return time