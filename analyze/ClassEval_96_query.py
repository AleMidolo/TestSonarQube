def query(self, weather_list, tmp_units='celsius'):
    """
        मौसम प्रणाली से शहर के मौसम और तापमान के लिए क्वेरी करें, और इनपुट पैरामीटर के आधार पर तापमान इकाइयों को परिवर्तित करें।
        :param weather_list: विभिन्न शहरों के लिए मौसम जानकारी का एक शब्दकोश, dict.
        :param tmp_units: परिवर्तित करने के लिए तापमान इकाइयाँ, str.
        :return: शहर का तापमान और मौसम, tuple.
        >>> weatherSystem = WeatherSystem('New York')
        >>> weather_list = {'New York': {'weather': 'sunny','temperature': 27,'temperature units': 'celsius'},'Beijing': {'weather': 'cloudy','temperature': 23,'temperature units': 'celsius'}}
        >>> weatherSystem.query(weather_list)
        (27, 'sunny')

        """
    if self.city not in weather_list:
        return None
    city_data = weather_list[self.city]
    self.weather = city_data['weather']
    self.temperature = city_data['temperature']
    current_units = city_data['temperature units']
    if tmp_units == 'fahrenheit' and current_units == 'celsius':
        self.temperature = self.celsius_to_fahrenheit()
    elif tmp_units == 'celsius' and current_units == 'fahrenheit':
        self.temperature = self.fahrenheit_to_celsius()
    return (self.temperature, self.weather)