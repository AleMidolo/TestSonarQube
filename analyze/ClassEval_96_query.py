def query(self, weather_list, tmp_units='celsius'):
    """
    查询天气系统以获取城市的天气和温度，并根据输入参数转换温度单位。
    :param weather_list: 不同城市天气信息的字典，dict。
    :param tmp_units: 要转换的温度单位，str。
    :return: 城市的温度和天气，tuple。
    >>> weatherSystem = WeatherSystem('New York')
    >>> weather_list = {'New York': {'weather': 'sunny','temperature': 27,'temperature units': 'celsius'},'Beijing': {'weather': 'cloudy','temperature': 23,'temperature units': 'celsius'}}
    >>> weatherSystem.query(weather_list)
    (27, 'sunny')

    """
    # Get the city's weather information from the weather_list
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