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
            temperature = (temperature * 9/5) + 32
        elif current_units == 'fahrenheit' and tmp_units == 'celsius':
            temperature = (temperature - 32) * 5/9
    
    return (temperature, weather)