def simulate_operation(self):
    """
    simula la operación del termostato. Iniciará automáticamente el método auto_set_mode para establecer el modo de operación,
    y luego ajustará automáticamente la temperatura actual de acuerdo con el modo de operación hasta que se alcance la temperatura objetivo.
    :return time: int, el tiempo que tomó completar la simulación.
    >>> thermostat = Thermostat(20.4, 37.5, 'cool')
    >>> thermostat.simulate_operation()
    18
    """
    self.auto_set_mode()
    
    time = 0
    
    while self.current_temp != self.target_temp:
        if self.mode == 'cool':
            if self.current_temp > self.target_temp:
                self.current_temp -= 1
            else:
                break
        elif self.mode == 'heat':
            if self.current_temp < self.target_temp:
                self.current_temp += 1
            else:
                break
        else:  # mode == 'off'
            break
        
        time += 1
    
    return time