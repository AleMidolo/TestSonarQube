def auto_check_conflict(self):
    """
        检查操作模式与当前温度和目标温度之间的关系是否存在冲突。
        如果存在冲突，操作模式将自动调整。
        :return: 如果模式与当前温度和目标温度之间的关系没有冲突，则返回 True，否则返回 False。
        >>> thermostat = Thermostat(20.4, 37.5, 'cool')
        >>> thermostat.auto_check_conflict()
        False
        >>> thermostat.mode
        'heat'
        """
    if self.mode == 'heat' and self.current_temperature >= self.target_temperature:
        self.mode = 'cool'
        return False
    elif self.mode == 'cool' and self.current_temperature <= self.target_temperature:
        self.mode = 'heat'
        return False
    else:
        return True