def simulate_operation(self):
    """
        模拟恒温器的操作。它将自动启动 auto_set_mode 方法以设置操作模式，
        然后根据操作模式自动调整当前温度，直到达到目标温度。
        :return time: int，完成模拟所需的时间。
        >>> thermostat = Thermostat(20.4, 37.5, 'cool')
        >>> thermostat.simulate_operation()
        18
        """
    self.auto_set_mode()
    time_elapsed = 0
    while abs(self.current_temperature - self.target_temperature) > 0.1:
        time.sleep(0.1)
        time_elapsed += 1
        if self.mode == 'heat':
            self.current_temperature += 1.0
        else:
            self.current_temperature -= 1.0
        if self.mode == 'heat' and self.current_temperature > self.target_temperature or (self.mode == 'cool' and self.current_temperature < self.target_temperature):
            self.current_temperature = self.target_temperature
    return time_elapsed