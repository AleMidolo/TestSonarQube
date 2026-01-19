def simulate_operation(self):
    """
    simula l'operazione del Termostato. Avvierà automaticamente il metodo auto_set_mode per impostare la modalità operativa,
    e poi regolerà automaticamente la temperatura attuale in base alla modalità operativa fino a raggiungere la temperatura target.
    :return time: int, il tempo impiegato per completare la simulazione.
    >>> thermostat = Thermostat(20.4, 37.5, 'cool')
    >>> thermostat.simulate_operation()
    18
    """
    # Imposta automaticamente la modalità operativa
    self.auto_set_mode()
    
    time = 0
    
    # Continua a regolare la temperatura fino a raggiungere il target
    while self.current_temp != self.target_temp:
        if self.mode == 'heat':
            # In modalità riscaldamento, aumenta la temperatura
            self.current_temp += 1
        elif self.mode == 'cool':
            # In modalità raffreddamento, diminuisce la temperatura
            self.current_temp -= 1
        
        time += 1
    
    return time