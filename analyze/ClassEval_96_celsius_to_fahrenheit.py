def celsius_to_fahrenheit(self):
    """
    Convierte la temperatura de Celsius a Fahrenheit.
    :return: la temperatura en Fahrenheit, float.
    >>> weatherSystem = WeatherSystem('Nueva York')
    >>> weatherSystem.temperature = 27
    >>> weatherSystem.celsius_to_fahrenheit()
    80.6

    """
    return (self.temperature * 9/5) + 32