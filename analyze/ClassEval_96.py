class WeatherSystem:
    def __init__(self, city) -> None:
        self.temperature = None
        self.weather = None
        self.city = city
        self.weather_list = {}
    
    def query(self, weather_list, tmp_units='celsius'):
        self.weather_list = weather_list
        if not self.city_in_weather_list():
            return False
        
        self.set_weather_data()
        
        if self.is_temperature_unit_different(tmp_units):
            return self.convert_temperature(tmp_units), self.weather
        
        return self.temperature, self.weather
    
    def set_city(self, city):
        self.city = city

    def celsius_to_fahrenheit(self):
        return (self.temperature * 9/5) + 32

    def fahrenheit_to_celsius(self):
        return (self.temperature - 32) * 5/9

    def city_in_weather_list(self):
        return self.city in self.weather_list

    def set_weather_data(self):
        self.temperature = self.weather_list[self.city]['temperature']
        self.weather = self.weather_list[self.city]['weather']

    def is_temperature_unit_different(self, tmp_units):
        return self.weather_list[self.city]['temperature units'] != tmp_units

    def convert_temperature(self, tmp_units):
        if tmp_units == 'celsius':
            return self.fahrenheit_to_celsius()
        elif tmp_units == 'fahrenheit':
            return self.celsius_to_fahrenheit()