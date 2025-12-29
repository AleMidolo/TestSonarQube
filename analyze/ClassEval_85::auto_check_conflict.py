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
    if self.current_temperature < self.target_temperature:
        if self.mode == 'heat':
            return True
        else:
            self.mode = 'heat'
            return False
    elif self.current_temperature > self.target_temperature:
        if self.mode == 'cool':
            return True
        else:
            self.mode = 'cool'
            return False
    else:
        return True