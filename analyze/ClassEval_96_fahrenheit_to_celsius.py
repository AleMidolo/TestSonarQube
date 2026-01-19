def fahrenheit_to_celsius(self):
    """
    Convierte la temperatura de Fahrenheit a Celsius.
    :return: la temperatura en Celsius, float.
    >>> weatherSystem = WeatherSystem('Nueva York')
    >>> weatherSystem.temperature = 80.6
    >>> weatherSystem.fahrenheit_to_celsius()
    26.999999999999996

    """
    return (self.temperature - 32) * 5 / 9