def query(self, weather_list, tmp_units = 'celsius'):
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
    # Get the city information from weather_list
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