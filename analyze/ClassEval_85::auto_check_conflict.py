def auto_check_conflict(self):
    """
    Controlla se c'è un conflitto tra la modalità operativa e la relazione tra la temperatura attuale e la temperatura target.
    Se c'è un conflitto, la modalità operativa verrà regolata automaticamente.
    :return: True se la modalità non è in conflitto con la relazione tra la temperatura attuale e la temperatura target, o False altrimenti.
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