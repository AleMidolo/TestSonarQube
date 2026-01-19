def fahrenheit_to_celsius(self):
    """
    将温度从华氏度转换为摄氏度。
    :return: 摄氏度的温度，浮点数。
    >>> weatherSystem = WeatherSystem('New York')
    >>> weatherSystem.temperature = 80.6
    >>> weatherSystem.fahrenheit_to_celsius()
    26.999999999999996

    """
    return (self.temperature - 32) * 5 / 9