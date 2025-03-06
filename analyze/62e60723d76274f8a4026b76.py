from datetime import time, timedelta

class Time:
    @classmethod
    def from_ticks(cls, ticks, tz=None):
        """
        Create a time from ticks (nanoseconds since midnight).

        :param ticks: nanoseconds since midnight
        :type ticks: int
        :param tz: optional timezone
        :type tz: datetime.tzinfo

        :rtype: Time

        :raises ValueError: if ticks is out of bounds
            (0 <= ticks < 86400000000000)
        """
        if not (0 <= ticks < 86400000000000):
            raise ValueError("ticks must be between 0 and 86400000000000")
        
        nanoseconds_per_second = 1_000_000_000
        nanoseconds_per_minute = 60 * nanoseconds_per_second
        nanoseconds_per_hour = 60 * nanoseconds_per_minute
        
        hours = ticks // nanoseconds_per_hour
        ticks %= nanoseconds_per_hour
        
        minutes = ticks // nanoseconds_per_minute
        ticks %= nanoseconds_per_minute
        
        seconds = ticks // nanoseconds_per_second
        ticks %= nanoseconds_per_second
        
        microseconds = ticks // 1000
        
        return time(hour=hours, minute=minutes, second=seconds, microsecond=microseconds, tzinfo=tz)