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
            # 加热模式：当前温度低于目标温度，每次增加1度
            self.current_temp += 1
        elif self.mode == 'cool':
            # 制冷模式：当前温度高于目标温度，每次降低1度
            self.current_temp -= 1
        else:
            # 如果模式为 'off' 或其他，则不调整温度
            break
        
        time += 1
    
    return time