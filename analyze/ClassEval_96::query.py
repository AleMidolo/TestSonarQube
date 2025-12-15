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
        Interroga il sistema meteorologico per ottenere il meteo e la temperatura della città, e converte le unità di temperatura in base al parametro di input.
        :param weather_list: un dizionario di informazioni meteorologiche per diverse città, dict.
        :param tmp_units: le unità di temperatura in cui convertire, str.
        :return: la temperatura e il meteo della città, tuple.
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
            return self.temperature, self.weather
        return None