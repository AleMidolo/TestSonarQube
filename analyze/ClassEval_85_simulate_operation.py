def simulate_operation(self):
    """
    模拟恒温器的操作。它将自动启动 auto_set_mode 方法以设置操作模式，
    然后根据操作模式自动调整当前温度，直到达到目标温度。
    :return time: int，完成模拟所需的时间。
    >>> thermostat = Thermostat(20.4, 37.5, 'cool')
    >>> thermostat.simulate_operation()
    18
    """
    # 首先调用 auto_set_mode 方法设置操作模式
    self.auto_set_mode()
    
    time = 0
    
    # 根据操作模式调整温度直到达到目标温度
    while self.current_temp != self.target_temp:
        if self.mode == 'heat':
            # 加热模式：当前温度低于目标温度，每次增加温度
            if self.current_temp < self.target_temp:
                self.current_temp += 0.5
                time += 1
            else:
                break
        elif self.mode == 'cool':
            # 冷却模式：当前温度高于目标温度，每次降低温度
            if self.current_temp > self.target_temp:
                self.current_temp -= 0.5
                time += 1
            else:
                break
        else:
            # 其他模式（如 'auto' 或无效模式）不进行温度调整
            break
        
        # 防止浮点数精度问题，当非常接近目标温度时直接设置为目标温度
        if abs(self.current_temp - self.target_temp) < 0.5:
            self.current_temp = self.target_temp
    
    return time