def set_city(self, city):
    """
    मौसम प्रणाली का शहर सेट करें।
    :param city: सेट करने के लिए शहर, str.
    :return: कुछ नहीं
    >>> weatherSystem = WeatherSystem('New York')
    >>> weatherSystem.set_city('Beijing')
    >>> weatherSystem.city
    'Beijing'

    """
    self.city = city