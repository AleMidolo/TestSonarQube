def auto_check_conflict(self):
    """
        Verifica si hay un conflicto entre el modo de operación y la relación entre la temperatura actual y la temperatura objetivo.
        Si hay un conflicto, el modo de operación se ajustará automáticamente.
        :return: True si el modo no está en conflicto con la relación entre la temperatura actual y la temperatura objetivo, o False en caso contrario.
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