def query(self, weather_list, tmp_units='celsius'):
    """
        Query the weather system for the weather and temperature of the city, and convert the temperature units based on the input parameter.
        :param weather_list: a dictionary of weather information for different cities, dict.
        :param tmp_units: the temperature units to convert to, str.
        :return: the temperature and weather of the city, tuple.
        >>> weatherSystem = WeatherSystem('New York')
        >>> weather_list = {'New York': {'weather': 'sunny', 'temperature': 27, 'temperature units': 'celsius'},
        ...                 'Beijing': {'weather': 'cloudy', 'temperature': 23, 'temperature units': 'celsius'}}
        >>> weatherSystem.query(weather_list)
        (27, 'sunny')
        """
    if self.city in weather_list:
        self.weather = weather_list[self.city]['weather']
        self.temperature = weather_list[self.city]['temperature']
        if tmp_units == 'fahrenheit':
            return (self.celsius_to_fahrenheit(), self.weather)
        return (self.temperature, self.weather)
    return None