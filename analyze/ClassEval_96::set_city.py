def set_city(self, city):
    """
        设置天气系统的城市。
        :param city: 要设置的城市，字符串类型。
        :return: None
        >>> weatherSystem = WeatherSystem('New York')
        >>> weatherSystem.set_city('Beijing')
        >>> weatherSystem.city
        'Beijing'

        """
    self.city = city