def get_target_temperature(self):
    """
        获取Thermostat类实例的目标温度。
        :return self.current_temperature: int
        >>> thermostat.get_target_temperature()
        37.5
        """
    return self.target_temperature