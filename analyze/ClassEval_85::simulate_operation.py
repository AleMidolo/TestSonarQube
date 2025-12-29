def simulate_operation(self):
    """
        simula l'operazione del Termostato. Avvierà automaticamente il metodo auto_set_mode per impostare la modalità operativa,
        e poi regolerà automaticamente la temperatura attuale in base alla modalità operativa fino a raggiungere la temperatura target.
        :return time: int, il tempo impiegato per completare la simulazione.
        >>> thermostat = Thermostat(20.4, 37.5, 'cool')
        >>> thermostat.simulate_operation()
        18
        """
    self.auto_set_mode()
    time_taken = 0
    while abs(self.current_temperature - self.target_temperature) > 0.1:
        if self.mode == 'heat':
            self.current_temperature += 1
        else:
            self.current_temperature -= 1
        time.sleep(1)
        time_taken += 1
    return time_taken