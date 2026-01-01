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
    if self.city in weather_list:
        weather_info = weather_list[self.city]
        self.weather = weather_info['weather']
        self.temperature = weather_info['temperature']
        if weather_info['temperature units'] == 'celsius' and tmp_units == 'fahrenheit':
            self.temperature = self.celsius_to_fahrenheit()
        elif weather_info['temperature units'] == 'fahrenheit' and tmp_units == 'celsius':
            self.temperature = self.fahrenheit_to_celsius()
        return (self.temperature, self.weather)
    return None