def celsius_to_fahrenheit(self):
    """
    तापमान को सेल्सियस से फारेनहाइट में परिवर्तित करें।
    :return: फारेनहाइट में तापमान, फ्लोट।
    >>> weatherSystem = WeatherSystem('New York')
    >>> weatherSystem.temperature = 27
    >>> weatherSystem.celsius_to_fahrenheit()
    80.6

    """
    return (self.temperature * 9/5) + 32