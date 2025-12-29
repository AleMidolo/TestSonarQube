def celsius_to_fahrenheit(self):
    """
        Convertire la temperatura da Celsius a Fahrenheit.
        :return: la temperatura in Fahrenheit, float.
        >>> weatherSystem = WeatherSystem('New York')
        >>> weatherSystem.temperature = 27
        >>> weatherSystem.celsius_to_fahrenheit()
        80.6

        """
    return self.temperature * 9 / 5 + 32