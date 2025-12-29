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
    if self.city not in weather_list:
        return (None, None)
    city_data = weather_list[self.city]
    self.weather = city_data['weather']
    self.temperature = city_data['temperature']
    current_units = city_data.get('temperature units', 'celsius')
    if tmp_units.lower() == 'fahrenheit' and current_units.lower() == 'celsius':
        self.temperature = self.celsius_to_fahrenheit()
    elif tmp_units.lower() == 'celsius' and current_units.lower() == 'fahrenheit':
        self.temperature = self.fahrenheit_to_celsius()
    return (self.temperature, self.weather)