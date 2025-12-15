class WeatherSystem: 
    def __init__(self, city) -> None:
        """
        Initialize the weather system with a city name.
        """
        self.temperature = None
        self.weather = None
        self.city = city
        self.weather_list = {}

    def set_city(self, city):
        """
        Set the city of the weather system.
        :param city: the city to set, str.
        :return: None
        >>> weatherSystem = WeatherSystem('New York')
        >>> weatherSystem.set_city('Beijing')
        >>> weatherSystem.city
        'Beijing'
        """
        self.city = city
    
    def celsius_to_fahrenheit(self):
        """
        Convert the temperature from Celsius to Fahrenheit.
        :return: the temperature in Fahrenheit, float.
        >>> weatherSystem = WeatherSystem('New York')
        >>> weatherSystem.temperature = 27
        >>> weatherSystem.celsius_to_fahrenheit()
        80.6
        """
        return (self.temperature * 9/5) + 32
    
    def fahrenheit_to_celsius(self):
        """
        Convert the temperature from Fahrenheit to Celsius.
        :return: the temperature in Celsius, float.
        >>> weatherSystem = WeatherSystem('New York')
        >>> weatherSystem.temperature = 80.6
        >>> weatherSystem.fahrenheit_to_celsius()
        26.999999999999996
        """
        return (self.temperature - 32) * 5/9
    
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
        if self.city in weather_list:
            weather_info = weather_list[self.city]
            self.weather = weather_info['weather']
            self.temperature = weather_info['temperature']
            if tmp_units == 'fahrenheit' and weather_info['temperature units'] == 'celsius':
                self.temperature = self.celsius_to_fahrenheit()
            return (self.temperature, self.weather)
        return None