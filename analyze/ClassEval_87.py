import datetime

class TimeUtils:

    TIME_FORMAT = "%H:%M:%S"
    DATE_FORMAT = "%Y-%m-%d"
    DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

    def __init__(self):
        self.current_datetime = datetime.datetime.now()

    def get_current_time(self):
        return self.format_datetime(self.current_datetime, self.TIME_FORMAT)

    def get_current_date(self):
        return self.format_datetime(self.current_datetime, self.DATE_FORMAT)

    def add_seconds(self, seconds):
        new_datetime = self.current_datetime + datetime.timedelta(seconds=seconds)
        return self.format_datetime(new_datetime, self.TIME_FORMAT)

    def string_to_datetime(self, string):
        return datetime.datetime.strptime(string, self.DATETIME_FORMAT)

    def datetime_to_string(self, dt):
        return dt.strftime(self.DATETIME_FORMAT)

    def get_minutes(self, string_time1, string_time2):
        time1 = self.string_to_datetime(string_time1)
        time2 = self.string_to_datetime(string_time2)
        return self.calculate_minutes_difference(time1, time2)

    def get_format_time(self, year, month, day, hour, minute, second):
        time_item = datetime.datetime(year, month, day, hour, minute, second)
        return self.format_datetime(time_item, self.DATETIME_FORMAT)

    def format_datetime(self, dt, fmt):
        return dt.strftime(fmt)

    def calculate_minutes_difference(self, time1, time2):
        return round((time2 - time1).seconds / 60)