from datetime import time, timedelta, tzinfo

class Time:
    def __init__(self, hour, minute, second, microsecond, tzinfo=None):
        self._hour = hour
        self._minute = minute
        self._second = second
        self._microsecond = microsecond
        self._tzinfo = tzinfo

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

        nanoseconds_per_hour = 3600 * 10**9
        nanoseconds_per_minute = 60 * 10**9
        nanoseconds_per_second = 10**9
        nanoseconds_per_microsecond = 10**3

        hours = ticks // nanoseconds_per_hour
        ticks %= nanoseconds_per_hour

        minutes = ticks // nanoseconds_per_minute
        ticks %= nanoseconds_per_minute

        seconds = ticks // nanoseconds_per_second
        ticks %= nanoseconds_per_second

        microseconds = ticks // nanoseconds_per_microsecond

        return cls(hours, minutes, seconds, microseconds, tz)