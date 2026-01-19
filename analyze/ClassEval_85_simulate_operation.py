def simulate_operation(self):
    """
        simula la operación del termostato. Iniciará automáticamente el método auto_set_mode para establecer el modo de operación,
        y luego ajustará automáticamente la temperatura actual de acuerdo con el modo de operación hasta que se alcance la temperatura objetivo.
        :return time: int, el tiempo que tomó completar la simulación.
        >>> thermostat = Thermostat(20.4, 37.5, 'cool')
        >>> thermostat.simulate_operation()
        18
        """
    start_time = time.time()
    self.auto_set_mode()
    while abs(self.current_temperature - self.target_temperature) > 0.1:
        if self.mode == 'heat':
            self.current_temperature += 0.1
        else:
            self.current_temperature -= 0.1
        time.sleep(0.1)
    end_time = time.time()
    return int(end_time - start_time)