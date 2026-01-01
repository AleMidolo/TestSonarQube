def query(self, weather_list, tmp_units='celsius'):
    """
        Interroga il sistema meteorologico per ottenere il meteo e la temperatura della città, e converte le unità di temperatura in base al parametro di input.
        :param weather_list: un dizionario di informazioni meteorologiche per diverse città, dict.
        :param tmp_units: le unità di temperatura in cui convertire, str.
        :return: la temperatura e il meteo della città, tuple.
        >>> weatherSystem = WeatherSystem('New York')
        >>> weather_list = {'New York': {'weather': 'sunny','temperature': 27,'temperature units': 'celsius'},'Beijing': {'weather': 'cloudy','temperature': 23,'temperature units': 'celsius'}}
        >>> weatherSystem.query(weather_list)
        (27, 'sunny')
        """
    if self.city in weather_list:
        self.weather = weather_list[self.city]['weather']
        self.temperature = weather_list[self.city]['temperature']
        if tmp_units == 'fahrenheit' and weather_list[self.city]['temperature units'] == 'celsius':
            self.temperature = self.celsius_to_fahrenheit()
        elif tmp_units == 'celsius' and weather_list[self.city]['temperature units'] == 'fahrenheit':
            self.temperature = self.fahrenheit_to_celsius()
        return (self.temperature, self.weather)
    return None