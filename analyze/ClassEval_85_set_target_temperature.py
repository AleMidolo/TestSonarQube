def set_target_temperature(self, temperature):
    """
    设置目标温度
    :param temperature: float, 目标温度
    >>> thermostat.set_target_temperature(37.6)
    >>> thermostat.target_temperature
    37.6
    """
    self.target_temperature = temperature