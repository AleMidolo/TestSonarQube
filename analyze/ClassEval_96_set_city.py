def set_city(self, city):
    """
        Imposta la città del sistema meteorologico.
        :param city: la città da impostare, str.
        :return: None
        >>> weatherSystem = WeatherSystem('New York')
        >>> weatherSystem.set_city('Beijing')
        >>> weatherSystem.city
        'Beijing'

        """
    self.city = city