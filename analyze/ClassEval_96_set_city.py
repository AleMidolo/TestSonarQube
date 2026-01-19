def set_city(self, city):
    """
        Establece la ciudad del sistema meteorológico.
        :param city: la ciudad a establecer, str.
        :return: None
        >>> weatherSystem = WeatherSystem('Nueva York')
        >>> weatherSystem.set_city('Pekín')
        >>> weatherSystem.city
        'Pekín'

        """
    self.city = city