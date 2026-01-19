def __init__(self, current_temp, target_temp, mode):
    """
    初始化恒温器
    :param current_temp: float, 当前温度
    :param target_temp: float, 目标温度
    :param mode: str, 操作模式 ('heat', 'cool', 'auto')
    """
    self.current_temp = current_temp
    self.target_temp = target_temp
    self.mode = mode