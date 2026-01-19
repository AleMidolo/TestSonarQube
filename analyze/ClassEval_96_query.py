def query(self, weather_list, tmp_units='celsius'):
    """
        Consulta el sistema meteorológico para obtener el clima y la temperatura de la ciudad, y convierte las unidades de temperatura según el parámetro de entrada.
        :param weather_list: un diccionario de información meteorológica para diferentes ciudades, dict.
        :param tmp_units: las unidades de temperatura a las que convertir, str.
        :return: la temperatura y el clima de la ciudad, tuple.
        >>> weatherSystem = WeatherSystem('New York')
        >>> weather_list = {'New York': {'weather': 'sunny','temperature': 27,'temperature units': 'celsius'},'Beijing': {'weather': 'cloudy','temperature': 23,'temperature units': 'celsius'}}
        >>> weatherSystem.query(weather_list)
        (27, 'sunny')

        """
    if self.city not in weather_list:
        return None
    city_data = weather_list[self.city]
    self.weather = city_data['weather']
    temperature = city_data['temperature']
    original_units = city_data['temperature units']
    if original_units == 'celsius' and tmp_units == 'fahrenheit':
        self.temperature = temperature
        temperature = self.celsius_to_fahrenheit()
    elif original_units == 'fahrenheit' and tmp_units == 'celsius':
        self.temperature = temperature
        temperature = self.fahrenheit_to_celsius()
    self.temperature = temperature
    return (temperature, self.weather)