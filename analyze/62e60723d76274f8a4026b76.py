from datetime import time, timedelta, tzinfo

class Time:
    def __init__(self, hour, minute, second, microsecond, tzinfo=None):
        self._time = time(hour, minute, second, microsecond, tzinfo)

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
        seconds_per_minute = 60
        minutes_per_hour = 60
        hours_per_day = 24

        total_seconds = ticks // nanoseconds_per_second
        nanoseconds = ticks % nanoseconds_per_second

        seconds = total_seconds % seconds_per_minute
        total_minutes = total_seconds // seconds_per_minute

        minutes = total_minutes % minutes_per_hour
        hours = total_minutes // minutes_per_hour

        if hours >= hours_per_day:
            hours = hours % hours_per_day

        microseconds = nanoseconds // 1000

        return cls(hours, minutes, seconds, microseconds, tz)