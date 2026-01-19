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
        return None
    
    city_data = weather_list[self.city]
    weather = city_data['weather']
    temperature = city_data['temperature']
    current_units = city_data['temperature units']
    
    # Convert temperature if needed
    if current_units != tmp_units:
        if current_units == 'celsius' and tmp_units == 'fahrenheit':
            temperature = (temperature * 9/5) + 32
        elif current_units == 'fahrenheit' and tmp_units == 'celsius':
            temperature = (temperature - 32) * 5/9
    
    return (temperature, weather)