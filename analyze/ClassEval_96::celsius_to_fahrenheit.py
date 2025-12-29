def celsius_to_fahrenheit(self):
    """
        将温度从摄氏度转换为华氏度。
        :return: 华氏度的温度，浮点数。
        >>> weatherSystem = WeatherSystem('New York')
        >>> weatherSystem.temperature = 27
        >>> weatherSystem.celsius_to_fahrenheit()
        80.6

        """
    return self.temperature * 9 / 5 + 32