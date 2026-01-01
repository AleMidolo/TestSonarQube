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
    if self.city in weather_list:
        self.weather = weather_list[self.city]['weather']
        self.temperature = weather_list[self.city]['temperature']
        if tmp_units == 'fahrenheit' and weather_list[self.city]['temperature units'] == 'celsius':
            self.temperature = self.celsius_to_fahrenheit()
        elif tmp_units == 'celsius' and weather_list[self.city]['temperature units'] == 'fahrenheit':
            self.temperature = self.fahrenheit_to_celsius()
        return (self.temperature, self.weather)
    else:
        return None