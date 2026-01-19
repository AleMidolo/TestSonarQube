def auto_set_mode(self):
    """
    通过与当前温度和目标温度进行比较，自动设置操作模式。如果当前温度低于目标温度，则操作模式设置为'heat'，否则设置为'cool'。
    >>> thermostat = Thermostat(20.4, 37.5, 'cool')
    >>> thermostat.auto_set_mode()
    >>> thermostat.mode
    'heat'
    """
    if self.current_temperature < self.target_temperature:
        self.mode = 'heat'
    else:
        self.mode = 'cool'