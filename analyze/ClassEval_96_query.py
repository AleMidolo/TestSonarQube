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
    # Get the city's weather information
    if self.city not in weather_list:
        return None
    
    city_info = weather_list[self.city]
    weather = city_info['weather']
    temperature = city_info['temperature']
    current_units = city_info['temperature units']
    
    # Convert temperature if needed
    if current_units != tmp_units:
        if current_units == 'celsius' and tmp_units == 'fahrenheit':
            temperature = temperature * 9/5 + 32
        elif current_units == 'fahrenheit' and tmp_units == 'celsius':
            temperature = (temperature - 32) * 5/9
    
    return (temperature, weather)