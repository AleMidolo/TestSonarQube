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

        nanoseconds = ticks
        microseconds = nanoseconds // 1000
        seconds = microseconds // 1000000
        microseconds = microseconds % 1000000
        minutes = seconds // 60
        seconds = seconds % 60
        hours = minutes // 60
        minutes = minutes % 60

        return cls(hours, minutes, seconds, microseconds, tz)