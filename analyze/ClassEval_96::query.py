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
    if self.city not in weather_list:
        return (None, None)
    city_data = weather_list[self.city]
    self.weather = city_data['weather']
    self.temperature = city_data['temperature']
    current_units = city_data.get('temperature units', 'celsius')
    if tmp_units == 'fahrenheit' and current_units == 'celsius':
        temp_fahrenheit = self.celsius_to_fahrenheit()
        return (temp_fahrenheit, self.weather)
    elif tmp_units == 'celsius' and current_units == 'fahrenheit':
        temp_celsius = self.fahrenheit_to_celsius()
        return (temp_celsius, self.weather)
    else:
        return (self.temperature, self.weather)