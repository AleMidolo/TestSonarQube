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
    # Check if current temperature is less than target temperature
    if self.current_temperature < self.target_temperature:
        # Need heating, but mode is 'cool' - conflict exists
        if self.mode == 'cool':
            self.mode = 'heat'
            return False
        # Mode is already 'heat' - no conflict
        return True
    # Check if current temperature is greater than target temperature
    elif self.current_temperature > self.target_temperature:
        # Need cooling, but mode is 'heat' - conflict exists
        if self.mode == 'heat':
            self.mode = 'cool'
            return False
        # Mode is already 'cool' - no conflict
        return True
    else:
        # Current temperature equals target temperature - no conflict
        return True