def query(self, weather_list, tmp_units='celsius'):
    """
        Query the weather system for the weather and temperature of the city,and convert the temperature units based on the input parameter.
        :param weather_list: a dictionary of weather information for different cities,dict.
        :param tmp_units: the temperature units to convert to, str.
        :return: the temperature and weather of the city, tuple.
        >>> weatherSystem = WeatherSystem('New York')
        >>> weather_list = {'New York': {'weather': 'sunny','temperature': 27,'temperature units': 'celsius'},'Beijing': {'weather': 'cloudy','temperature': 23,'temperature units': 'celsius'}}
        >>> weatherSystem.query(weather_list)
        (27, 'sunny')

        """
    if self.city not in weather_list:
        return (None, None)
    city_data = weather_list[self.city]
    self.weather = city_data['weather']
    temperature = city_data['temperature']
    current_units = city_data['temperature units']
    if tmp_units.lower() == 'fahrenheit' and current_units.lower() == 'celsius':
        self.temperature = temperature
        temperature = self.celsius_to_fahrenheit()
    elif tmp_units.lower() == 'celsius' and current_units.lower() == 'fahrenheit':
        self.temperature = temperature
        temperature = self.fahrenheit_to_celsius()
    else:
        self.temperature = temperature
    return (temperature, self.weather)