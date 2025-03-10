from datetime import time, timedelta, tzinfo

class Time(time):
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

        nanoseconds = ticks % 1000
        microseconds = (ticks // 1000) % 1000
        milliseconds = (ticks // 1000000) % 1000
        seconds = (ticks // 1000000000) % 60
        minutes = (ticks // 60000000000) % 60
        hours = (ticks // 3600000000000) % 24

        return cls(hours, minutes, seconds, milliseconds * 1000 + microseconds, tzinfo=tz)