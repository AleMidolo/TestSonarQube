from datetime import time, timedelta

class Time:
    def __init__(self, hour, minute, second, microsecond, tzinfo=None):
        self._time = time(hour, minute, second, microsecond, tzinfo)

    @classmethod
    def from_ticks(cls, ticks, tz=None):
        """
        Crea un'istanza di tempo a partire dai ticks (nanosecondi trascorsi dalla mezzanotte).

        :param ticks: nanosecondi trascorsi dalla mezzanotte
        :type ticks: int
        :param tz: fuso orario opzionale
        :type tz: datetime.tzinfo

        :rtype: Time

        :raises ValueError: se il valore di ticks è fuori dai limiti
            (0 <= ticks < 86400000000000)
        """
        if not (0 <= ticks < 86400000000000):
            raise ValueError("ticks must be between 0 and 86400000000000")

        nanoseconds_in_second = 1_000_000_000
        nanoseconds_in_minute = 60 * nanoseconds_in_second
        nanoseconds_in_hour = 60 * nanoseconds_in_minute

        hours = ticks // nanoseconds_in_hour
        ticks %= nanoseconds_in_hour

        minutes = ticks // nanoseconds_in_minute
        ticks %= nanoseconds_in_minute

        seconds = ticks // nanoseconds_in_second
        ticks %= nanoseconds_in_second

        microseconds = ticks // 1000

        return cls(hours, minutes, seconds, microseconds, tz)