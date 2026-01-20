def simulate_operation(self):
    """
    simula la operación del termostato. Iniciará automáticamente el método auto_set_mode para establecer el modo de operación,
    y luego ajustará automáticamente la temperatura actual de acuerdo con el modo de operación hasta que se alcance la temperatura objetivo.
    :return time: int, el tiempo que tomó completar la simulación.
    >>> thermostat = Thermostat(20.4, 37.5, 'cool')
    >>> thermostat.simulate_operation()
    18
    """
    # Establecer el modo de operación automáticamente
    self.auto_set_mode()
    
    time = 0
    
    # Ajustar la temperatura hasta alcanzar el objetivo
    while self.current_temp != self.target_temp:
        if self.mode == 'cool':
            # En modo enfriamiento, aumentar la temperatura actual
            self.current_temp += 1
        elif self.mode == 'heat':
            # En modo calentamiento, disminuir la temperatura actual
            self.current_temp -= 1
        
        time += 1
    
    return time