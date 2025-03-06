import datetime

class Time:
    def __init__(self, hour, minute, second, microsecond, tzinfo=None):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.microsecond = microsecond
        self.tzinfo = tzinfo

    @classmethod
    def from_ticks(cls, ticks, tz=None):
        if not (0 <= ticks < 86400000000000):
            raise ValueError("Ticks must be between 0 and 86400000000000")
        
        microseconds = ticks // 1000
        seconds, microseconds = divmod(microseconds, 1000000)
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        
        return cls(hours, minutes, seconds, microseconds, tz)