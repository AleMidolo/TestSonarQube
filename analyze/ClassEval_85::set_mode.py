def set_mode(self, mode):
    """
        获取当前工作模式
        :param mode: str, 工作模式。仅限 ['heat', 'cool']
        >>> thermostat.set_mode('cool')
        >>> thermostat.mode
        'cool'
        """
    if mode in ['heat', 'cool']:
        self.mode = mode
    else:
        raise ValueError("Mode must be either 'heat' or 'cool'")