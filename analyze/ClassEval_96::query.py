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
    if tmp_units == current_units:
        self.temperature = temperature
        return (temperature, self.weather)
    if tmp_units == 'celsius' and current_units == 'fahrenheit':
        self.temperature = (temperature - 32) * 5 / 9
        return (self.temperature, self.weather)
    elif tmp_units == 'fahrenheit' and current_units == 'celsius':
        self.temperature = temperature * 9 / 5 + 32
        return (self.temperature, self.weather)
    else:
        self.temperature = temperature
        return (temperature, self.weather)