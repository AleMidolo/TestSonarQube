def fahrenheit_to_celsius(self):
    """
    तापमान को फ़ारेनहाइट से सेल्सियस में परिवर्तित करें।
    :return: सेल्सियस में तापमान, फ्लोट।
    >>> weatherSystem = WeatherSystem('New York')
    >>> weatherSystem.temperature = 80.6
    >>> weatherSystem.fahrenheit_to_celsius()
    26.999999999999996

    """
    return (self.temperature - 32) * 5 / 9